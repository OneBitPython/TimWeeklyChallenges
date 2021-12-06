l = (
    lambda n: [1, 1, 2, 6, 4][n]
    if n < 5
    else l(q := n // 5) * 2 ** (q % 4) * l(n % 5) % 10
)
for i in [I := input] * int(I()):
    print(l(int(I())))
