import heapq
def Dijkstra(edge,start,v):
    d = [float('inf')]*v
    d[start] = 0
    pq = [(0,start)]
    heapq.heapify(pq)
    while pq:
        dist,p = heapq.heappop(pq)
        if dist > d[p]:continue
        for to,cost in edge[p].items():
            if d[to] <= dist + cost:continue
            d[to] = dist + cost
            heapq.heappush(pq, (d[to], to))
    return d
