from collections import deque

def BFS(v, start, path):
    que = deque([start])
    d = [float('inf')]*v
    d[start] = 0
    while que:
        p = que.popleft()
        for nxt in path[p]:
            if d[nxt] != float('inf'):continue
            d[nxt] = d[p] + 1
            que.append(nxt)
    return d

def BFSrestration(v, start, end, path):
    que = deque([start])
    d = [float('inf')]*v
    d[start] = 0
    while que:
        p = que.popleft()
        for nxt in path[p]:
            if d[nxt] != float('inf'):
                continue
            d[nxt] = d[p] + 1
            que.append(nxt)
    dist = d[end]
    route = [0]*(dist + 1)

    now = end
    for i in range(dist)[::-1]:
        route[i+1] = now
        for nxt in path[now]:
            if d[nxt] == dist - 1:
                now = nxt
                dist -= 1
                break
    route[0] = start
    return route
