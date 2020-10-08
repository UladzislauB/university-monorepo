#include <fstream>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>

using namespace std;

const long long INF = 922337203685477580;

ifstream in("input.txt");
ofstream out("output.txt");

int main(){
    int n, m, u, v, w;
    in >> n >> m;
    vector< vector <pair <int, int> > > g(n);
    for (int i=0; i<m; i++) {
        in >> u >> v >> w;
        u--;
        v--;
        if (u == v) {
            continue;
        }
        g[u].push_back(make_pair(v, w));
        g[v].push_back(make_pair(u, w));
    }

    vector<long long> d(n, INF);
    d[0] = 0;
    priority_queue<pair<long long, int>> q;
    q.push(make_pair(0, 0));

    while (!q.empty()) {
        pair<long long, int> top = q.top();
        q.pop();
        long long cur_d = - top.first;
        int v = top.second;
        if (d[v] < cur_d)
            continue;


        for (int j=0; j<g[v].size(); j++) {
            int to = g[v][j].first;
            long long len = g[v][j].second;
            if (d[to] > d[v] + len) {
                d[to] = d[v] + len;
                q.push(make_pair(-d[to], to));
            }
        }
    }
    out << d[n - 1];
    return 0;
}
