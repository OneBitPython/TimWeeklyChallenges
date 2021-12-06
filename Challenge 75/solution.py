for _ in [I := input] * (int(I())):
    r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    n = I()
    print(
        r[n[-1]]
        + sum(
            [r[n[i]] if r[n[i]] >= r[n[i + 1]] else -r[n[i]] for i in range(len(n) - 1)]
        )
    )
