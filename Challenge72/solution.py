for _ in [W := input] * int(W()):
    s = W()
    b = True
    for i in range(1, ((l := len(s)) // 2) + 1):
        if l % i == 0:
            h = [int(s[j : j + i]) for j in range(0, l, i)]
            for q in range(len(h) - 1):
                if h[q] + 1 != h[q + 1]:
                    break
            else:
                print(True)
                b = False
                break
    if b:
        print(False)
