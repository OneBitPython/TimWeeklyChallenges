#include <bits/stdc++.h>
using namespace std;

#define endl "\n"
#define int long long
#define all(v) v.begin(), v.end()
#define pb push_back

vector<vector<int>> adj;
vector<bool>visited;

void dfs(int u, int &sz){
    visited[u] = 1;
    sz++;
    for(int &v : adj[u]){
        if(!visited[v])dfs(v, sz);
    }
}

void solve(){
    int n, m;
    cin >> n >> m;
    adj.resize(n+1);
    visited.resize(n+1);
    for(int i = 0;i<m;++i){
        int u,v;
        cin >> u >> v;
        adj[u].pb(v);
        adj[v].pb(u);
    }
    int sz = 0;
    dfs(1, sz);
    cout << (sz == n?"YES":"NO") << endl;
    adj.clear();
    visited.clear();
}


int32_t main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int t;
    cin >> t;
    while(t--)solve();
}