import sys
sys.stdin = open('input.txt','r')

def catch(i):
    q = list()
    visited = [0] * (N + 1)
    q.append((i, 0))
    visited[i] = 1
    num = 1
    d = 0

    while q:
        result = q.pop(0)
        a = result[0]
        if result[1] == D:
            pass
        else:
            d = result[1]+1
            if gang(a):
                for i in gang(a):
                    if visited[i] == 0:
                        q.append((i, d))
                        visited[i] = 1
                        num += 1
    return num


T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 조직원 수
    D = int(input())    # 검거일자
    C = int(input())    # 간선 수
    max_start, max_arrest = -1, -1    # 제일 많이 잡히는 시작점, 그때 잡힌 인원

    gang = [[] for _ in range(N+1)]
    for _ in range(C):
        S, E = map(int, input().split())
        gang[S].append(E)

    for i in range(1, N+1):
        if max_arrest < catch(i):
            max_arrest = catch(i)
            max_start = i

    print('#{} {} {}'.format(tc, max_start, max_arrest))







