# -*- coding: utf-8 -*-
"""genshen_cp_skin.repo —— 把某一套 CP 铺到本地，并取它需要的文件。

取文件按「离线优先」的顺序：
  1. 包内自带（packs/cpNN/）—— 源图与引擎代码都在包里，不联网、不需要 git
  2. 本地已铺开的副本     —— ~/.genshen-cp-skin/<repo>/
  3. 源仓库（网络）       —— 只有可选件才走这里：VSIX、吉祥物、缩略图

源仓库仍然保留（https://github.com/WPH666-py/Genshen-skin-CPN），
它承担两件事：素材版权页、以及可选件的上游。

本地根目录：`~/.genshen-cp-skin/`（可用 GENSHEN_CP_HOME 覆盖）。
"""
import io
import json
import os
import shutil
import sys

from . import mirror, proxy

OWNER = "WPH666-py"
BRANCH = "main"
RAW_HOST = "https://raw.githubusercontent.com"

DEFAULT_HOME = os.path.join(os.path.expanduser("~"), ".genshen-cp-skin")
MARKER_NAME = ".genshen-bundled"
TIMEOUT = 60
_last_good = {}


def home_dir():
    return os.path.abspath(os.path.expanduser(
        os.environ.get("GENSHEN_CP_HOME") or DEFAULT_HOME))


def skin_dir(repo):
    return os.path.join(home_dir(), repo)


# ---------------------------------------------------------------------------
# 包内自带那一层
# ---------------------------------------------------------------------------
def packs_dir():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "packs")


def pack_root(pack):
    """该套在包内的目录。"""
    return os.path.join(packs_dir(), pack["pack_dir"])


def bundled_files(pack):
    """该套随包自带的文件（相对该套根目录）。"""
    return list((pack.get("bundled") or {}).get("file_list") or [])


def bundled_path(pack, rel):
    rel = rel.replace("\\", "/")
    full = os.path.join(pack_root(pack), rel.replace("/", os.sep))
    return full if os.path.isfile(full) else None


def materialize(pack, quiet=False):
    """把包内自带的该套文件铺到 `~/.genshen-cp-skin/<repo>/`，返回目标目录。

    CP 的安装脚本要求一个真实的仓库目录树（`src/<pkg>/engine/...`），
    所以这里铺的是完整结构，而不只是"能读到文件"。
    """
    dst = skin_dir(pack["repo"])
    files = bundled_files(pack)
    if not files:
        return None
    marker = os.path.join(dst, MARKER_NAME)
    if os.path.isfile(marker):
        if all(os.path.isfile(os.path.join(dst, r.replace("/", os.sep))) for r in files):
            return dst
    n = 0
    for rel in files:
        src = os.path.join(pack_root(pack), rel.replace("/", os.sep))
        if not os.path.isfile(src):
            continue
        out = os.path.join(dst, rel.replace("/", os.sep))
        os.makedirs(os.path.dirname(out), exist_ok=True)
        try:
            shutil.copy2(src, out)
            n += 1
        except OSError:
            pass
    try:
        from . import __version__
        ver = __version__
    except Exception:
        ver = "0"
    with io.open(marker, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps({"repo": pack["repo"], "id": pack["id"],
                            "files": n, "version": ver}, ensure_ascii=False) + "\n")
    if not quiet:
        print("[gc] 使用包内自带素材铺开 %s（%d 个文件，离线可用）" % (pack["id"], n))
    return dst


def is_ready(pack):
    """该套是否已铺开（包内素材到位）。"""
    files = bundled_files(pack)
    if not files:
        return False
    dst = skin_dir(pack["repo"])
    if not os.path.isfile(os.path.join(dst, MARKER_NAME)):
        return False
    return all(os.path.isfile(os.path.join(dst, r.replace("/", os.sep))) for r in files)


# ---------------------------------------------------------------------------
# 网络（只在取可选件时用到）
# ---------------------------------------------------------------------------
def _http_get(url, timeout=TIMEOUT, want_json=False):
    import urllib.request
    req = urllib.request.Request(url, headers={
        "User-Agent": "genshen-cp-skin/%s" % _version(), "Accept": "*/*"})
    with proxy.opener().open(req, timeout=timeout) as r:
        data = r.read()
    if want_json:
        return json.loads(data.decode("utf-8"))
    return data


def _version():
    try:
        from . import __version__
        return __version__
    except Exception:
        return "0"


def fetch_raw(pack, path, binary=True, timeout=TIMEOUT):
    """取该套源仓库里的一个文件（先包内，再本地，最后联网）。"""
    data = None
    p = bundled_path(pack, path)
    if p:
        with open(p, "rb") as f:
            data = f.read()
    if data is None:
        local = os.path.join(skin_dir(pack["repo"]), path.replace("/", os.sep))
        if os.path.isfile(local):
            with open(local, "rb") as f:
                data = f.read()
    if data is None:
        import urllib.error
        import urllib.parse
        quoted = urllib.parse.quote(path)
        errors = []
        cands = mirror.raw_candidates(OWNER, pack["repo"], BRANCH, quoted)
        good = _last_good.get("raw")
        if good:
            cands.sort(key=lambda t: 0 if t[0] == good else 1)
        for label, url in cands:
            try:
                data = _http_get(url, timeout=timeout)
            except urllib.error.HTTPError as e:
                errors.append("%s: HTTP %s" % (label, e.code))
                continue
            except Exception as e:
                errors.append("%s: %s" % (label, type(e).__name__))
                continue
            if not data:
                errors.append("%s: 空响应" % label)
                continue
            _last_good["raw"] = label
            break
        else:
            raise RuntimeError("下载 %s/%s 失败，尝试过的通道：\n  %s"
                               % (pack["repo"], path, "\n  ".join(errors)))
    return data if binary else data.decode("utf-8", "replace")


def fetch_text(pack, path):
    return fetch_raw(pack, path, binary=False)


def download_to(pack, path, dest, quiet=False):
    """取一个文件到 dest（自动建目录）。包内命中时不联网。"""
    from_bundle = bundled_path(pack, path) is not None
    data = fetch_raw(pack, path)
    os.makedirs(os.path.dirname(os.path.abspath(dest)), exist_ok=True)
    with open(dest, "wb") as f:
        f.write(data)
    if not quiet:
        print("[gc] %s %s -> %s (%.1f KB)"
              % ("包内" if from_bundle else "下载", path, dest, len(data) / 1024.0))
    return dest


def rmtree(path):
    """删除目录树（Windows 安全版：先清只读位）。"""
    import stat as _stat
    if not path or not os.path.exists(path):
        return True

    def _on_error(func, p, _exc):
        try:
            os.chmod(p, _stat.S_IWRITE)
            func(p)
        except Exception:
            pass

    try:
        shutil.rmtree(path, onerror=_on_error)
    except Exception:
        pass
    return not os.path.exists(path)


def last_good():
    return dict(_last_good)
