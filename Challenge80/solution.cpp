#include <bits/stdc++.h>
using namespace std;
#define side_type tuple<int, int, int, int>
#define polygon_type vector<pair<int, int>>
#define pb push_back

void getInput(polygon_type &vec, int &N)
{
    string comma = ",";
    for (int j = 0; j < N; ++j)
    {
        string tmp;
        cin >> tmp;

        int pos;
        while ((pos = tmp.find(comma)) != string::npos)
        {
            vec.pb({stoi(tmp.substr(0, pos)), stoi(tmp.substr(pos + 1, tmp.size()))});
            tmp.clear();
        }
    }
}

void AddSides(polygon_type &polygon, vector<side_type> &sides)
{
    for (int i = 0; i < polygon.size() - 1; i++)
    {
        sides.pb(side_type(polygon[i].first, polygon[i].second, polygon[i + 1].first, polygon[i + 1].second));
    }
    sides.pb(side_type(polygon.back().first, polygon.back().second, polygon[0].first, polygon[0].second));
}

//ngl, this function is a c++ version of the python code from wiki
bool PIP(int x, int y, polygon_type &polygon)
{
    int j = polygon.size() - 1;
    bool c = false;
    for (int i = 0; i < polygon.size(); ++i)
    {
        if (x == polygon[i].first && y == polygon[i].second)
        {
            return true;
        }
        if (polygon[i].second > y != polygon[j].second > y)
        {
            int slope = (x - polygon[i].first) * (polygon[j].second - polygon[i].second) - (polygon[j].first - polygon[i].first) * (y - polygon[i].second);
            if (slope == 0)
            {
                return true;
            }
            if (slope < 0 != (polygon[j].second < polygon[i].second))
            {
                c = !c;
            }
        }
        j = i;
    }
    return c;
}

void solve()
{
    int N;
    cin >> N;
    polygon_type polygon1, polygon2;

    getInput(polygon1, N);
    getInput(polygon2, N);

    vector<side_type> first_polygon_sides, second_polygon_sides;

    AddSides(polygon1, first_polygon_sides);
    AddSides(polygon2, second_polygon_sides);

    bool br = false;
    double a, b, c, d, w, x, y, z, dx0, dx1, dy0, dy1;
    for (auto side1 : first_polygon_sides)
    {
        if (br)
        {
            break;
        }
        for (auto side2 : second_polygon_sides)
        {
            tie(a, b, c, d) = side1;
            tie(w, x, y, z) = side2;
            dx0 = c - a;
            dx1 = y - w;
            dy0 = d - b;
            dy1 = z - x;
            //this formula is from stackoverflow(only this formula)
            if ((dy1 * (y - a) - dx1 * (z - b)) * (dy1 * (y - c) - dx1 * (z - d)) < 0 && (dy0 * (c - w) - dx0 * (d - x)) * (dy0 * (c - y) - dx0 * (d - z)) < 0)
            {
                br = true;
                break;
            }
        }
    }
    if (br)
    {
        cout << "true" << endl;
    }
    else
    {
        for (auto side : polygon1)
        {
            if (PIP(side.first, side.second, polygon2))
            {
                br = true;
                break;
            }
        }
        if (br)
        {
            cout << "true" << endl;
        }
        else
        {
            for (auto side : polygon2)
            {
                if (PIP(side.first, side.second, polygon1))
                {
                    br = true;
                    break;
                }
            }
            string a = br == 0 ? "false" : "true";
            cout << a << endl;
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i)
    {
        solve();
    }
}
