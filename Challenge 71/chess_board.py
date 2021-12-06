for i in range(int(input())):
    q = input()
    print(
        True
        if abs((h := "abcdefgh").index(q[0]) - h.index(q[3]))
        == abs(int(q[1]) - int(q[4]))
        else False
    )
