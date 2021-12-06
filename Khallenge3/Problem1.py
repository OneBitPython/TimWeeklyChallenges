G=[];M=str.split
for L in [I:=input]*int(I()):G.append(I())
e=M(I());A=enumerate;Q=[];C=lambda x:{(q:=M(z,":"))[0]:q[1] for z in M(x)}
for i,j in A(G):
    j=C(j);k=[n for n in j if j[n]=="0" and n in e];o=[];P=[]
    for l in k:
        if o:=[abs(a-i) for a,b in A(G) if C(b)[l]=="1"]:P.append(min(o));o = []
    Q.append(max(P)) if P else Q.append(0)
print(Q.index(min(Q)))