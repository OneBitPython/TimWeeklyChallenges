#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;
    vector<int> height(n);
    for(int i = 0;i<n;++i)cin >> height[i];
    int pt1=0, pt2=height.size()-1,tmp;
    int max=0;
    while(pt1<pt2){
        tmp = min(height[pt1], height[pt2]);
        if ((pt2-pt1)*tmp > max){
            max = (pt2-pt1)*tmp;
        }
        if (height[pt1]>height[pt2]){
            pt2--;
        }else{
            pt1++;
        }
    }
    cout << max << endl;
}

int main(){
    int t;
    cin >> t;
    while(t--)solve();
    
}
