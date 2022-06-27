# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   call_input_print.py
@Author  :   Billy Zhou
@Time    :   2022/06/23
@Desc    :   None
'''


import sys
from pathlib import Path
cwdPath = Path(__file__).parents[1]  # the num depend on your filepath
sys.path.append(str(cwdPath))

from src.input_print import input_print, input_print_nested
# from importlib import reload
# import src.input_print


def call_print_input_nested():
    # reload(src.input_print) # reload the module
    print('calling input_print_nested()')
    input_print_nested()
    print('calling input_print()')
    input_print()


if __name__ == '__main__':
    call_print_input_nested()
