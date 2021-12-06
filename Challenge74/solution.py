for _ in [H := input] * (int(H())):
    n = list(map(int, H().split()))
    t = True
    f = False
    v = f
    for S in n:
        O = [f] * (L := len(n))
        Y = n.index(S)
        while all(O) == f:
            if O[Y] == t:
                break
            else:
                O[Y] = t
                Q = n[Y]
                X = Q - (L * (Q // L))
                if X < 0:
                    Y += X
                Y = Y + X if Y + X < L else X - (L - Y)
        if n[0] == 0 and L == 1:
            v = f
            break
        if Y == n.index(S) and all(O):
            v = t
            break
    print(v)
