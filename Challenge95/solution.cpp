#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define int long long

int MXN = 1000000;
vector<bool>prime(MXN,1);
vector<int>primes;
void preprocess(int n)
{
    for (int p = 2; p * p <= n; p++)
    {
        if (prime[p] == true)
        {
            for (int i = p * p; i <= n; i += p)
                prime[i] = false;
        }
    }
    for (int p = 2; p <= n; p++)
        if (prime[p])
            primes.pb(p);
}

void solve(){

    int v;
    cin >> v;
    cout << primes[v] << endl;
}

int32_t main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    preprocess(MXN);
    int t;
    cin >> t;
    while(t--)solve();
}