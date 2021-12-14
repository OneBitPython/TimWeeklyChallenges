def solution():
    # for i in[I:=input]*int(I()):print(*[v[1:]+v[0]+"ay"for v in I().split()])
    runner = int(input())
    for run in range(runner):
        sentence = input()
        for words in sentence.split(" "):
            word = list(words)
            word[-1] = f"{word[-1]}{word[0]}ay"
            word.pop(0)
            print(" ".join(word), end=" ")    
        print()
