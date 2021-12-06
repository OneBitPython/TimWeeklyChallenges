for j in[I:=input]*int(I()):
 f,g=0,0;
 for i in(s:=I().split()):x,y=map(float,i.split(","));f+=x;g+=y
 print(f"{round(f/(c:=len(s)))},{round(g/c)}"))