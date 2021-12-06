T = int(input())
for _ in range(T):
    string = input()
    ans = ""
    for i in range(0, len(string), 2):
        try:
            ans += int(string[i]) * string[i + 1]
        except:
            pass
    print(ans)
