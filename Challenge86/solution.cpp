#include <bits/stdc++.h>
using namespace std;

bool won(vector<bool> &grid){
    vector<tuple<int, int, int>> pos_wins = {
        {0, 1, 2},
        {3, 4, 5},
        {6, 7, 8},
        {0, 4, 8},
        {2, 4, 6},
        {0, 3, 6},
        {1, 4, 7},
        {2, 5, 8},
    };
    for(auto x : pos_wins){
        int a,b,c;
        tie(a,b,c) = x;
        if(grid[a]&&grid[b]&&grid[c]){
            return true;
        }
    }
    return false;


}
void solve(){
    char start;
    int n;
    cin >> start >> n;

    vector<int> arr(n);
    for(int i=0;i<n;++i) cin >> arr[i];
    vector<bool> grid(9);
    vector<bool> grid2 = grid;
    for(auto instr : arr){
        instr--;
        if(start=='X') grid[instr] = 1;
        else grid2[instr]=1;
        
        if(won(grid)||won(grid2)){
            cout << start << endl;
            return;
        }
        start = start=='X'?'O':'X';
    }
    cout << "Tie" << endl;
}
int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
}