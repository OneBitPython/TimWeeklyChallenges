def solution():
    for _ in range(int(input())):
        W, H = map(int, input().split())
        arr = []
        for q in range(H):
            arr.append(list(map(int, input().split())))
        rivers = []
        visited = [[False for _ in v] for v in arr]
        for x in range(len(arr)):
            for y in range(W):
                i, j = x, y
                queue = [[i, j]]
                sizes = 0
                while len(queue) > 0:
                    i, j = queue.pop(0)
                    if not visited[i][j]:
                        visited[i][j] = True
                        if arr[i][j] == 1:
                            neighbours = []
                            sizes += 1
                            if i > 0:
                                neighbours.append([i-1, j])
                            if i < len(arr)-1:
                                neighbours.append([i+1, j])
                            if j > 0:
                                neighbours.append([i, j-1])
                            if j < len(arr[0])-1:
                                neighbours.append([i, j+1])
                            for q in neighbours:
                                if not visited[q[0]][q[1]]:
                                    queue.append(q)
                if sizes > 0:
                    rivers.append(sizes)
        print(*sorted(rivers))
