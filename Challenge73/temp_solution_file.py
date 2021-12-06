def solution():
    for _ in [I := input] * int(I()):
        N = int(I())
        H = I()
        A = []
        l = I()
        p = []
        for Z in l:
            p.append(int(Z))
        A.append(p)
        for v in range((N // (O := len(A[0]))) - 1):
            p = []
            for Z in I():
                p.append(int(Z))
            A.append(p)
        c = False
        for a, b in enumerate(A):
            if c:
                break
            for i, j in enumerate(b):
                if j == 2:
                    Y = (a + 1, i + 1)
                    c = True
                    break
        m = []
        for a, b in enumerate(A):
            for i, j in enumerate(b):
                if j == 1:
                    if H == "L":
                        l = [(a + 1, 0)]
                    elif H == "D":
                        l = [(len(A) + 1, 1), (len(A) + 1, O)]
                    elif H == "R":
                        l = [(a + 1, O + 1)]
                    else:
                        l = [(0, 1), (0, O)]
                    R = (a + 1, i + 1)
                    n = []
                    for z in l:
                        n.append(abs(R[0] - z[0]) + abs(R[1] - z[1]))
                    T = min(n)
                    if Y[0] == R[0]:
                        Q = abs(Y[0] - R[0]) + abs(Y[1] - R[1])
                        W = Q
                    else:
                        Q = abs(Y[0] - R[0]) + (O - Y[1]) + (O - R[1])
                        W = abs(Y[0] - R[0]) + abs(1 - Y[1]) + abs(1 - R[1])
                    m.append([min(Q + T, W + T), min(Q, W)])
        print(min(m, key=lambda x: (x[0], x[1]))[1])
