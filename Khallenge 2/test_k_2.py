"""
How to use?
Import your solution in line 71, and run this script
If you see some weird chars instead of colors in output or don't want colors
switch COLOR_OUT to False in line 16
"""

import sys
import platform
from time import perf_counter
from typing import Callable
from unittest import mock
from io import StringIO
from tests import test_inp, test_out

COLOR_OUT = True

def enable_win_term_mode() -> bool:
    win = platform.system().lower() == 'windows'
    if win == False:
        return True

    from ctypes import windll, c_int, byref, c_void_p
    ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
    INVALID_HANDLE_VALUE = c_void_p(-1).value
    STD_OUTPUT_HANDLE = c_int(-11)

    hStdout = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    if hStdout == INVALID_HANDLE_VALUE:
        return False

    mode = c_int(0)
    ok = windll.kernel32.GetConsoleMode(c_int(hStdout), byref(mode))
    if not ok:
        return False

    mode = c_int(mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING)
    ok = windll.kernel32.SetConsoleMode(c_int(hStdout), mode)
    if not ok:
        return False
    
    return True

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio  # free up some memory
        sys.stdout = self._stdout


@mock.patch("builtins.input", side_effect=[str(len(test_out))] + test_inp)
def test_challenge_k_2(input: Callable) -> None:
    color_out = COLOR_OUT and enable_win_term_mode()

    red, green, yellow, cyan, reset = (
        "\x1b[31m",
        "\x1b[32m",
        "\x1b[33m",
        "\x1b[36m",
        "\x1b[0m",
    ) if color_out else [""] * 5

    with Capturing() as output:
        start = perf_counter()

        import water_pipes    # change this to your file name with solution without .py extension

        end = perf_counter()

    passed = i = 0
    for i in range(1, len(test_out) + 1):
        out, exp, inp = output[i - 1], test_out[i - 1], test_inp[i - 1]
        if str(out) != str(exp):
            print(f"Test nr:{i}\n      Input: {cyan}{inp}{reset}")
            print(f"Your output: {red}{out}{reset}")
            print(f"   Expected: {green}{exp}{reset}")
        else:
            passed += 1

    print(f"\nPassed: {green if passed == i else red}{passed}/{i}{reset} tests")
    print(f"Finished in: {yellow}{end - start:.4f}{reset} seconds")


if __name__ == "__main__":
    test_challenge_k_2()
