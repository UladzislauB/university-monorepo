#include <fstream>
#include <queue>
#include <vector>
#include <utility>


using namespace std;

ifstream in("flow.in");
ofstream out("flow.out");

const int INF = 2000000;

int n, m, s, t;
vector<int> d;
vector<vector<pair<int, int>>> g;
vector<vector<int>> f;
vector<int> ptr;

bool bfs() {
   for (int j=0; j<n; j++)
        d[j] = -1;
    d[s] = 0;
    queue <int> q;
    q.push(s);

    while(!q.empty()) {
        int v = q.front();
        q.pop();
        for (int j=0; j<g[v].size(); j++) {
            int u = g[v][j].first, c_vu = g[v][j].second;
            if (d[u] == -1 && f[v][u] < c_vu) {
                d[u] = d[v] + 1;
                q.push(u);
            }
        }
    }
    return d[t] != -1;
}


int dfs(int v, int flow) {
    if (flow == 0 || v == t)
        return flow;
    for (int j=ptr[v]; j<g[v].size(); j++) {
        int u = g[v][j].first, c = g[v][j].second;
        if (d[u] != d[v] + 1)  {
            ptr[v] ++;
            continue;
        }

        int block_flow = dfs(u,min(flow, c-f[v][u]));
        f[u][v] -= block_flow;
        f[v][u] += block_flow;
        if (block_flow != 0)
            return block_flow;
        ptr[v] ++;
    }
    return 0;
}




int main() {

    in >> n >> m >> s >> t;
    s--;
    t--;
    g.resize(n);

    queue<pair<int, int>> order_q;

    for (int i=0; i<m; i++) {
        int u,v,c;
        in >> u >> v >> c;
        u--;
        v--;
        order_q.push(make_pair(u,v));
        g[u].push_back(make_pair(v, c));
        g[v].push_back(make_pair(u, 0));
    }

    d.resize(n,-1);
    f.resize(n, vector <int> (n, 0));
    ptr.resize(n, 0);

    int ans_flow =0;

    while(bfs()) {
        for (int i=0; i<n; i++)
            ptr[i] = 0;
        int curr_flow = 0;
        do {
            curr_flow = dfs(s,INF);
            ans_flow += curr_flow;
        } while (curr_flow != 0);
    }

    out << ans_flow <<endl;
    while (!order_q.empty()){
        int r = order_q.front().first, col = order_q.front().second;
        order_q.pop();
        out<<f[r][col]<<endl;
    }
    return 0;
}
