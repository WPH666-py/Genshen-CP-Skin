# -*- coding: utf-8 -*-
"""让 `python -m genshen_cp_skin` 等价于 `gc`。"""
import sys

from .cli import main

if __name__ == "__main__":
    sys.exit(main())
