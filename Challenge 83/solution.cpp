#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    cin >> T;
    cin.ignore(10000, '\n');
    while (T--){
        string s,tmp,ans;
        getline(cin,s);
        stringstream ss(s);
        while(ss >> tmp){
            ans+=tmp.substr(1)+tmp[0]+"ay ";
        }
        cout << ans.substr(0,ans.length()-1) << endl;
    }
}