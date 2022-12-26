import sys
sys.stdin = open('input.txt', 'r')

f = open('C:/Users/PX/Desktop/algo/output.txt', 'w')
# 조직원수 : 5 ~ 500
# 데이 : 8일

def search(c, v):  # 큐로 구현
    global cnt
    global D
    v[c] = 1
    que = []
    for i in li[c]:
        que.append((i, cnt))
    while que:
        w = que.pop(0)
        if w[1] != D:
            if v[w[0]] != 1:
                for i in li[w[0]]:
                    que.append((i, w[1] + 1))
                v[w[0]] = 1
        elif w[1] == D:
            continue
    num = 0
    for i in v:
        num += i
    return num


T = int(input())  # 테케 수

for tc in range(1, T + 1):
    member = int(input())  # 인원값
    D = int(input())  # 데이 수
    L = int(input())  # 라인수
    nums = [list(map(int, input().split())) for i in range(L)]  # 조직원 관계
    li = [[] for i in range(member + 1)]  # 조직원과의 관계표현 리스트
    for i in nums:
        start, end = i[0], i[1]  # start, end로 받기
        li[start].append(end)  # 조직원 관계 저장
    ans_li = []
    for i in range(1, member + 1):  # bruteforce 탐색
        ans = []
        cnt = 0
        visit = [0] * (member + 1)
        ans_li.append(search(i, visit))  # 함수 실행
    max_num = 0
    top = 0
    for i in range(len(ans_li)):
        if max_num < ans_li[i]:
            max_num = ans_li[i]
            top = i + 1
    print(tc, top, max_num)
    f.write('#{} {} {}\n'.format(tc, top, max_num))