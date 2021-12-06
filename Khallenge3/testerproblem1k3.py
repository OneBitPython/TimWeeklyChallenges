"""
How to use?
Import your solution in line 92, and run this script
If you see some weird chars instead of colors in output or don't want colors
switch COLOR_OUT to False in line 30

WARNING: My tester ignores printing in input() but official tester FAILS if you
        print something in input()
        Don't do that: input("What is the test number?") 
        Use empty input: input()

Some possible errors:
    - None in "Your output": Your solution didn't print for all cases.
    - None in "Input": Your solution print more times then there is cases.
    - If you see None in "Input" or "Your output" don't check failed cases until
        you fix problem with printing, cos "Input" and "Your output" are misaligned
        after first missing/extra print
    - StopIteration: Your solution try to get more input then there is test cases
"""

from itertools import zip_longest
import sys
import platform
from time import perf_counter
from typing import Callable
from unittest import mock
from io import StringIO
from i3_1 import inp as inp_
from o3_1 import outp as test_out

COLOR_OUT = True

test_inp = []
for t in inp_:
    test_inp.append(str(t[0]))
    test_inp += [*t[1]]
    test_inp.append(t[2])


def enable_win_term_mode() -> bool:
    win = platform.system().lower() == "windows"
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
def test_challenge(input: Callable) -> None:
    color_out = COLOR_OUT and enable_win_term_mode()

    red, green, yellow, cyan, reset = (
        (
            "\x1b[31m",
            "\x1b[32m",
            "\x1b[33m",
            "\x1b[36m",
            "\x1b[0m",
        )
        if color_out
        else [""] * 5
    )

    with Capturing() as output:
        start = perf_counter()

        import Problem1  # change this to your file name with solution without .py extension

        end = perf_counter()

    from pprint import pprint

    print("Started testing:")
    print(f" - Number of cases: {cyan}{len(test_out)}{reset}")
    print(
        f" - Average length of blocks: {yellow}{sum(x[0] for x in inp_) // len(test_out):_}{reset}"
    )
    print(f" - Max length of blocks: {yellow}{max(x[0] for x in inp_):_}{reset}")
    print(
        f" - Average length of facilities: {yellow}{sum(len(x[1][0].split()) for x in inp_) // len(test_out):_}{reset}"
    )
    print(
        f" - Max length of facilities: {yellow}{max(len(x[1][0].split()) for x in inp_):_}{reset}\n"
    )

    passed = i = 0
    for i, (out, exp, inp) in enumerate(zip_longest(output, test_out, inp_), 1):
        if out != str(exp):
            print(f"Test nr:{i}\n      Input: {cyan}")
            pprint(inp)
            print(f"{reset}Your output: {red}{out}{reset}")
            print(f"   Expected: {green}{exp}{reset}\n")
        else:
            passed += 1

    print(f"Passed: {green if passed == i else red}{passed}/{i}{reset} tests")
    print(f"Finished in: {yellow}{end - start:.4f}{reset} seconds")


if __name__ == "__main__":
    test_challenge()
