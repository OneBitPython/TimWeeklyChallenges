#include <bits/stdc++.h>
using namespace std;
using namespace std::chrono;
#include <chrono>
#define int long long

int check(int x, int y)
{
    int t = 1;
    while (x >= t*y)
    {
        t = t * y;
    }
    if (x<y) return 1;
    int output = 0;
    while (t)
    {
        if(x/t!=1) return 0;
        output++;
        x -= t*(x/t);
        t /= y;
    }

    return output;
}
void solve(){
    int n;
    cin >> n;
    int j = n-1;
    int best = 0,v,ans;
    for(int i=2;i<=sqrt(j);++i){
        if(j%i==0){
            v = check(n,i);
            if(v){
                if(v > best){
                    best = v;ans=i;
                }
            }
            if(j/i!=i){
                v=check(n,j/i);
                if(v){
                    if(v>best){
                        best = v;ans=j/i;
                    }
                }
            }
        }
    }
    if(best==0)cout<<n-1<<endl;
    else cout << ans<<endl;
}
int32_t main(){
    int t;
    cin >> t;
    while(t--) solve();
}