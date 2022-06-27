# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_call_input_print.py
@Author  :   Billy Zhou
@Time    :   2022/06/23
@Desc    :   None
'''


import sys
from pathlib import Path
cwdPath = Path(__file__).parents[1]  # the num depend on your filepath
sys.path.append(str(cwdPath))

import unittest
import io
from unittest.mock import patch
from src.call_input_print import call_print_input_nested


class TestCallInputPrint(unittest.TestCase):
    """A simple TestCase to help u understand where to patch"""

    # @unittest.skip('stop')
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_call_print_input_nested(self, mock_stdout, mock_input):
        """only patch the builtins function input()

        Parameters:
        ====
            mock_stdout:
                patched by @patch('sys.stdout', new_callable=io.StringIO)
            mock_input:
                patched by @patch('builtins.input')"""

        # mock functions
        mock_input.return_value = 'builtins.input is patched'

        # start test
        call_print_input_nested()
        self.assertEqual(mock_stdout.getvalue(), ''.join([
            'calling input_print_nested()\n',
            'input_print_nested() is called\n',
            'input_print() is called\n',
            'builtins.input is patched\n',
            'calling input_print()\n',
            'input_print() is called\n',
            'builtins.input is patched\n'
        ]))

        # output the mock msg
        sys.stdout = sys.__stdout__
        print(mock_input.mock_calls)
        print(f'called time: {mock_input.call_count}')
        print('test_call_print_input_nested is over\n')

    # @unittest.skip('stop')
    @patch('builtins.input')
    @patch('src.call_input_print.input_print')
    @patch('src.call_input_print.input_print_nested')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_call_print_input_nested_imported(self, mock_stdout, mock_input_print_nested_caller, mock_input_print_caller, mock_input):
        """patch both functions imported in the module call_input_print

        Parameters:
        ====
            mock_stdout:
                patched by @patch('sys.stdout', new_callable=io.StringIO)
            mock_input_print_nested_caller:
                patched by @patch('src.call_input_print.input_print_nested')
            mock_input_print_caller:
                patched by @patch('src.call_input_print.input_print')
            mock_input:
                patched by @patch('builtins.input')"""

        # mock functions
        mock_input.return_value = 'builtins.input is patched'

        def side_effect():
            # msg for testing
            sys.stdout = sys.__stdout__
            print('mocking input_print() imported in src.call_input_print')
            print(f'called time: {mock_input_print_caller.call_count}')
            sys.stdout = mock_stdout

            # mock input_print()
            print('mock_input_print_caller() is called')
            print(mock_input('mock_input() called by mock_input_print_caller()'))
        mock_input_print_caller.side_effect = side_effect

        def side_effect_nested():
            # msg for testing
            sys.stdout = sys.__stdout__
            print('mocking input_print_nested() imported in src.call_input_print')
            print(f'called time: {mock_input_print_nested_caller.call_count}')
            sys.stdout = mock_stdout

            # mock input_print_nested()
            print('mock_input_print_nested_caller() is called')
            return mock_input_print_caller()
        mock_input_print_nested_caller.side_effect = side_effect_nested

        # start test
        call_print_input_nested()
        self.assertEqual(mock_stdout.getvalue(), ''.join([
            'calling input_print_nested()\n',
            'mock_input_print_nested_caller() is called\n',
            'mock_input_print_caller() is called\n',
            'builtins.input is patched\n',
            'calling input_print()\n',
            'mock_input_print_caller() is called\n',
            'builtins.input is patched\n'
        ]))

        # output the mock msg
        sys.stdout = sys.__stdout__
        print(mock_input.mock_calls)
        print(f'called time: {mock_input.call_count}')
        print('test_call_print_input_nested_imported is over\n')

    # @unittest.skip('stop')
    @patch('builtins.input')
    @patch('src.input_print.input_print')
    @patch('src.input_print.input_print_nested')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_call_print_input_nested_defined(self, mock_stdout, mock_input_print_nested_callee, mock_input_print_callee, mock_input):
        """patch both functions defined in the module input_print

        Parameters:
        ====
            mock_stdout:
                patched by @patch('sys.stdout', new_callable=io.StringIO)
            mock_input_print_nested_callee:
                patched by @patch('src.input_print.input_print_nested')
            mock_input_print_callee:
                patched by @patch('src.input_print.input_print')
            mock_input:
                patched by @patch('builtins.input')"""

        # mock functions
        mock_input.return_value = 'builtins.input is patched'

        def side_effect():
            # msg for testing
            sys.stdout = sys.__stdout__
            print('mocking input_print() defined in src.input_print')
            print(f'called time: {mock_input_print_callee.call_count}')
            sys.stdout = mock_stdout

            # mock input_print()
            print('mock_input_print_callee() is called')
            print(mock_input('mock_input() called by mock_input_print_callee()'))
        mock_input_print_callee.side_effect = side_effect

        def side_effect_nested():
            # msg for testing
            sys.stdout = sys.__stdout__
            print('mocking input_print_nested() defined in src.input_print')
            print(f'called time: {mock_input_print_nested_callee.call_count}')
            sys.stdout = mock_stdout

            # mock input_print_nested()
            print('mock_input_print_nested_callee() is called')
            return mock_input_print_callee()
        mock_input_print_nested_callee.side_effect = side_effect_nested

        # start test
        call_print_input_nested()
        self.assertEqual(mock_stdout.getvalue(), ''.join([
            'calling input_print_nested()\n',
            'input_print_nested() is called\n',
            'mock_input_print_callee() is called\n',
            'builtins.input is patched\n',
            'calling input_print()\n',
            'input_print() is called\n',
            'builtins.input is patched\n'
        ]))

        # output the mock msg
        sys.stdout = sys.__stdout__
        print(mock_input.mock_calls)
        print(f'called time: {mock_input.call_count}')
        print('test_call_print_input_nested_defined is over\n')


if __name__ == '__main__':
    unittest.main()
