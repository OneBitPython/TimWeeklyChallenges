#include <bits/stdc++.h>
using namespace std;


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int I,W,H;cin>>I;
    for(int q=0;q<I;++q)
    {
        cin>>W>>H;
        vector<int>rivers;
        vector<bool>tmp;
        vector<vector<int>>arr;
        vector<int>row;
        queue<pair<int,int>>queue1;
        queue<pair<int,int>>neighbours;
        int i,j,sizes,G;
        for(int B=0;B<H;++B){row={};for (int V=0;V<W;++V){cin>>G;row.push_back(G);}arr.push_back(row);}
        vector<vector<bool>> visited(arr.size(), vector<bool>(arr[0].size(),false));
        // for(int i=0;i<arr.size();++i){tmp={};for(int j=0;j<arr[i].size();++j){tmp.push_back(0);}visited.push_back(tmp);}
        for(int x=0;x<arr.size();++x)
        {for (int y=0;y<arr[x].size();++y){i=x;j=y;queue1.push({i,j});sizes=0;
                while(queue1.size()>0)
                {
                    i=queue1.front().first;j=queue1.front().second;queue1.pop();
                    if (!visited[i][j])
                    {
                        visited[i][j]=1;
                        if (arr[i][j]==1)
                        {
                            sizes++;
                            if (i>0){neighbours.push({i-1,j});}
                            if (i<arr.size()-1){neighbours.push({i+1,j});}
                            if(j>0){neighbours.push({i,j-1});}
                            if(j<arr[0].size()-1){neighbours.push({i, j+1});}
                            while(!neighbours.empty())
                            {
                                int one = neighbours.front().first;
                                int second  = neighbours.front().second;
                                if (!visited[one][second]){queue1.push({one,second});}
                                neighbours.pop();
                            }
                        }
                    }
                }
                if(sizes>0){rivers.push_back(sizes);}
            }
        }
        sort(rivers.begin(), rivers.end());
        string value = "";
        for(auto val:rivers){value+=to_string(val)+" ";}
        cout<<value.substr(0, value.size()-1)<<endl;
    }
}
