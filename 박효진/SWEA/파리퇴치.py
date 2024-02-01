T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_block = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_fly = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    sum_fly += arr[x][y]
            if sum_fly > max_block:
                max_block = sum_fly
    print(f'#{test_case} {max_block}')