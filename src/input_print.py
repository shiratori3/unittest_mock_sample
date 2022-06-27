# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   input_print.py
@Author  :   Billy Zhou
@Time    :   2022/06/23
@Desc    :   None
'''


import sys
from pathlib import Path
cwdPath = Path(__file__).parents[1]  # the num depend on your filepath
sys.path.append(str(cwdPath))


def input_print():
    print('input_print() is called')
    print(input('input() called by input_print()'))


def input_print_nested():
    print('input_print_nested() is called')
    return input_print()


if __name__ == '__main__':
    input_print_nested()
