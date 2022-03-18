#include <bits/stdc++.h>
using namespace std;
void solve(){
    
    int n, m;
    cin >>m >> n;
    vector<vector<int>> arr(n, vector<int>(m, 0));
    for(int i = 0;i<n;++i){
        for(int j = 0;j<m;++j) cin >> arr[i][j];
    }
    int prev_length = 0;
    int area = 0;
    for(int x = 0;x<n;++x){
        for(int y = 0;y<m;++y){
            int i = x, j = y;
            int width = 1, height = 1;

            if(arr[i][j] == 1){
                for(int w = j+1;w<m;++w){
                    if(arr[i][w]==1) width++;
                    else break;
                }
                for(int h = i+1;h<n;++h){
                    int cwidth = 0;
                    for(int w = j;w<m;++w){
                        if(arr[h][w] == 1)cwidth++;
                        else break;
                    }
                    if(cwidth >= width) height++;
                    else break;
                }
                for(int h = i-1;h>=0;--h){
                    int cwidth = 0;
                    for(int w = j;w<m;++w){
                        if(arr[h][w] == 1)cwidth++;
                        else break;
                    }
                    if(cwidth >= width) height++;
                    else break;
                }

                area = max(area, height*width);
                
            }
        }
    }
    cout << area << endl;
}

int main(){
    ios_base::sync_with_stdio(false);
    cout.tie(NULL);
    cin.tie(NULL);
    int t;
    cin >> t;
    while(t--) solve();
}