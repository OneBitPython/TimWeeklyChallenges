q = input
for _ in range(int(q())):
    r, _ = map(int, q().split())
    A = []
    for _ in range(r):
        A.append(list(map(int, input().split())))
    k = []
    for i in range(len(A) - 1):
        g = A[i]
        for j in range(len(g) - 1):
            k.append(
                str(g[j]) + str(g[j + 1]) + str(A[i + 1][j]) + str(A[i + 1][j + 1])
            )
    print(len(list(set(k))))
