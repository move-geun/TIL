import sys
sys.stdin = open('input.txt')

def BFS(n,visited):
    global arr
    global answer
    global D
    global p
    d = 0
    queue = [n]
    while d <= D:
        new_queue = []
        for q in queue:
            visited.append(q)
            if arr[q] != 0:
                new_queue += arr[q]
        new_queue = list(set(new_queue))
        queue = new_queue
        visited = list(set(visited))
        d += 1
    if len(visited) > answer:
        answer = len(visited)
        p = n
    return

T = int(input())
for t in range(T):
    N = int(input())
    D = int(input())
    C = int(input())
    arr = [0] * (N+1)
    answer = 0
    p = 0
    for c in range(C):
        a,b = map(int,input().split(' '))
        if arr[a] == 0:
            arr[a] = [b]
        else:
            arr[a].append(b)
    for n in range(1,N+1):
        visited = []
        BFS(n,visited)
    print(p,answer)