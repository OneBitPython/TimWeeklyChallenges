for _ in range(int(input())):
    A = list(map(int, input().split()))
    print(
        sum(
            [
                q - A[i]
                for i in range(1, len(A) - 1)
                if A[i] < (q := min(max(A[:i]), max(A[i + 1 :])))
            ]
        )
    )
