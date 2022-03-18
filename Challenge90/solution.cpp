#include <bits/stdc++.h>
using namespace std;

#pragma GCC optimize("Ofast")
#pragma GCC target("avx,avx2,fma")

#define all(c) c.begin(), c.end()

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t;
    cin >> t;
    while(t--){
        string a, b;
        cin >> a >> b;

        string ans;
        int l1 = a.size()-1;
        int l2 = b.size()-1;
        int c = 0;
        while (l1>=0 || l2>=0 || c){
            if(l1> -1){
                c+=a[l1]-'0';
                l1--;
            }
            if(l2 > -1){
                c+=b[l2]-'0';
                l2--;
            }
            ans+=(c%2+'0');
            c >>= 1;
        }
        reverse(all(ans));
        cout << ans << endl;
    }
    
}