#include<queue>
#include<iostream>
#include<utility>
#include<functional>

const long long INF = 0x1fffffffffffffff;

std::vector<long long> Dijkstra(std::vector<std::vector<std::pair<int, long long>>>& edge, const int& start){
    int v = edge.size();
    std::vector<long long> d(v,INF);
    d.at(start) = 0;
    std::priority_queue<std::pair<long long, int>,std::vector<std::pair<long long, int>>,std::greater<std::pair<long long, int>>> pq;
    pq.push({0,start});
    while(!pq.empty()){
        long long dist = pq.top().first;
        int p = pq.top().second;
        pq.pop();
        if(dist > d.at(p)) continue;
        for(int i = 0; i<int(edge.at(p).size()); i++){
            int to = edge.at(p).at(i).first;
            long long cost = edge.at(p).at(i).second;
            if(d.at(to) <= dist + cost)continue;
            d.at(to) = dist + cost;
            pq.push({d.at(to),to});
        }
    }
    return d;
}
