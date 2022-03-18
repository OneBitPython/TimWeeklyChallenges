#include <bits/stdc++.h>
using namespace std;

#define int long long
#define pb push_back
#define all(v) v.begin(), v.end()
#define endl "\n"

int MXN = (int)(1e7)+1;
vector<bool>prime(MXN,1);
void preprocess(int n){
    for (int p = 2; p * p <= n; p++)
    {
        if (prime[p] == true)
        {
            for (int i = p * p; i <= n; i += p)
                prime[i] = false;
        }
    }
}

void solve(){
    string s;
    cin >> s;
    sort(all(s));
    int n = stoi(s);
    int ans = prime[n]?n:0;
    while(next_permutation(all(s))){
        int x = stoi(s);
        if(prime[x]){
            if(x > ans)ans = x;
        }
    }
    cout << ans << endl;
}

int32_t main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    preprocess(MXN);
    int t;
    cin >> t;
    while(t--)solve();
}