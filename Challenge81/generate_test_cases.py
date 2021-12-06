import math
import random
import string
import json
import gzip
# from tqdm import tqdm
from pathlib import Path

from challenge81generator import solution
path = Path(__file__).parent


def generate_tests(number_of_cases: int, max_len: int, compress: bool) -> None:
    test_inputs = []
    test_expected = []
    for _ in range(number_of_cases):
        cur_len = random.randint(1, max_len)
        num = "0"
        while num[0] == "0":
            num = "".join(random.choices(string.digits, k=cur_len))
        t = [num]

        test_inputs.append(t)
        test_expected.append(solution(t))


    cases = [test_inputs, test_expected]

    if compress:
        content = bytes(json.dumps(cases), "utf-8")
        with gzip.open(path / "test_cases_s.json.gz", "wb", compresslevel=9) as g:
            g.write(content)
    else:

        with open(path / "test_cases_large.json", "w") as f:
            json.dump(cases, f, indent=2)


if __name__ == "__main__":
    generate_tests(number_of_cases=500, max_len=1000, compress=True)
