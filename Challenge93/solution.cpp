#include <bits/stdc++.h>
using namespace std;

int MXN  = (int)(1e5);
bitset<(int)(1e5+5)>access;
void solve(){
    int n, k, b;
    cin >> n >> k >> b;
    access.reset();
    for(int i = 0;i<b;++i){
        int v;
        cin >> v;
        access[v] = 1;
    }
    vector<int> prefix;
    int to_fix = 0;
    for(int i = 1;i<=n;++i){
        if(access[i])to_fix++;
        prefix.push_back(to_fix);
    }
    int res = 1e9;
    for(int i = 0;i<=n-k;++i){
        int cost;
        if(i == 0){
            cost = prefix[i+k-1];
            res = min(res, cost);
            continue;
        }
        cost = prefix[i+k-1] - prefix[i-1];
        res = min(res, cost);
    }
    cout << res << endl;
}

int main(){
    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t;
    cin >> t;
    while(t--)solve();
    
}