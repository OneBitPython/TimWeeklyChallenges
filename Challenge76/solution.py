for _ in [I := input] * int(I()):
    F = "".join(i + dict(T="A", A="T", G="C", C="G")[i] for i in I())
    S = [
        [sum(1 for a, b in zip(F, i[0]) if a == b), i[1]]
        for i in [I().split() for _ in range(int(I()))]
    ]
    print(" ".join(sorted(i[1] for i in S if i[0] == max(i[0] for i in S))))
# for _ in[I:=input]*int(I()):F="".join(i+dict(T="A",A="T",G="C",C="G")[i]for i in I());S=[[sum(1 for a,b in zip(F,i[0])if a==b),i[1]] for i in[I().split()for _ in range(int(I()))]];print(" ".join(sorted(i[1]for i in S if i[0]==max(i[0]for i in S))))
