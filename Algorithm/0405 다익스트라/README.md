### 다익스트라 구현



* 다익스트라란?

  * 노드와 간선이 주어질 때, 시작 지점부터 특정 지점 or 끝부분, 최적의 경로를 찾을 수 있는 방법

  * heap 모듈을 통해, 구현 가능하지만, 일단 안쓰고 해보자

    ```python
    
    # 다익스트라 공부
    
    
    # 노드에 대한 간선정보가 입력되지 않았을 때, 무한으로 값을 주기 위해 선언
    INF = int(1e9)
    
    # 문제 풀이에 필요한 노드, 간선의 개수 받아오기
    n, m = map(int, input().split())
    
    # 시작노드 번호 받기
    start = int(input())
    
    # 각 노드, 간선 정보를 담을 리스트
    graph = [[] for i in range(n+1)]
    
    # 방문(=이미 조사를 끝낸)하였는지 체크 리스트
    visited = [False]*(n+1)
    
    # 최단거리 테이블을 모두 무한으로 초기화
    distance = [INF]*(n+1)
    
    # 모든 간선정보 입력받기
    for _ in range(m):
        a, b, c = map(int, input().split())
        # a번 노드에서 b까지 가는데 c 비용이 든다.
        # 도착지와 비용을 a 인덱스 자리에 튜플형태로 저장
        graph[a].append((b, c))
    
    # 방문하지 않은 노드들 중에 최소 거리가 가장 작은 노드를 우선 탐색한다.
    # 그래서 해당 노드의 인덱스를 가져올 함수 작성
    def get_small_node():
        min_value = INF
        # index == return 값, 미리 초기화 해준거임
        index = 0
        for i in range(1, n+1):
            if distance[i] < min_value and not visited[i]:
                min_value = distance[i]
                index = i
        return index
    
    # 다익스트라 함수
    def dijkstra(start):
        # 시작노드에서 초기화 == 시작노드의 최소 거리는 0이고 방문했다
        distance[start] = 0
        visited[start] = True
        # 시작 노드와 연결된 모든 노드의 정보를 distance 리스트로 갱신한다.
        for j in graph[start]:
            distance[j[0]] = j[1]
        # 시작 노드를 제외한 전체 n-1개의 노드에 대해 조사하는데
        # 최소 거리가 가장 작은 노드를 우선탐색하니까, 그거 찾는거
        for i in range(n-1):
            now = get_small_node()
            visited[now] = True
            # 현재 노드와 연결된 노드를 확인
            for j in graph[now]:
                cost = distance[now] + j[1]
                # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[j[0]]:
                    distance[j[0]] = cost
    
    # 다익스트라 실행
    dijkstra(start)
    
    # 모든 노드로 가기 위한 최단 거리를 출력
    for i in range(1, n+1):
        # 도달할 수 없는 경우
        if distance[i] == INF:
            print('못감~')
        # 도달할 수 있는 경우
        else:
            print(distance[i])
    
    
    ```

    