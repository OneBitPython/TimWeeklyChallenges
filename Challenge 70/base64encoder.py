for _ in range(int(input())):s=input().replace("=","");b="".join([f"{'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'.index(i):06b}" for i in s]);print(*[chr(int(v, 2)) for i in range(0,len(b),8) if len(v:=b[i:i+8]) == 8],sep="")
#for _ in range(int(input())):s=input().replace("=","");b="".join([f"{'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'.index(i):06b}" for i in s]);print(*[chr(int(v, 2)) for i in range(0,len(b),8) if len(v:=b[i:i+8]) == 8],sep="")
