def solution():
    #include <bits/stdc++.h>
    using namespace std;
    
    /**
    
    1
    asdZ 12349
    0.5
    */
    void print() { cout << endl; };
    template <typename T, typename... args>
    void print(T one, args... rest)
    {
        cout << one << " ";
        print(rest...);
    }
    
    void insert_into_keyboard(map<char, pair<int, int>> &keyboard, string line, int idx)
    {
        for (int i = 0; i < line.size(); ++i)
        {
            keyboard[line[i]] = {idx, i};
        }
    }
    void solve(map<char, pair<int, int>> &keyboard)
    {
        vector<pair<int, int>> space_bar = {{4, 3}, {4, 4}, {4, 5}, {4, 6}, {4, 7}};
        string s;
        double speed;
    
        cin.ignore(256, '\n'); // remaining input characters up to the next newline character
    
        getline(cin, s);
        cin >> speed;
    
        char prev_value = s.front(), current_value;
        int currx, curry, prevx, prevy, keyx = 4, keyy = 3, cx = 2, cy = 0;
        double ans = 0;
    
        bool caps_lock_on = isupper(prev_value) ? 1 : 0;
        if (caps_lock_on)
        {
            prev_value = '.';
        }
    
        for (int i = 0; i < s.size(); ++i)
        {
            current_value = s[i];
            if (current_value != ' ')
            {
                tie(currx, curry) = keyboard[tolower(current_value)];
            }
            else
            {
                tie(currx, curry) = {keyx, keyy};
            }
            if (prev_value == '.')
            {
                tie(prevx, prevy) = {cx, cy};
            }
            else
            {
                if (prev_value == ' ')
                {
                    tie(prevx, prevy) = {keyx, keyy};
                }
                else
                {
                    tie(prevx, prevy) = keyboard[tolower(prev_value)];
                }
            }
            if (isupper(current_value) && caps_lock_on == 0)
            {
                ans += abs(prevx - cx) + abs(prevy - cy);
                tie(prevx, prevy) = {cx, cy};
                prev_value = '.';
                caps_lock_on = 1;
            }
            if (islower(current_value) && caps_lock_on)
            {
                ans += abs(prevx - cx) + abs(prevy - cy);
                tie(prevx, prevy) = {cx, cy};
                prev_value = '.';
                caps_lock_on = 0;
            }
            if (current_value != ' ')
            {
                if (prev_value == ' ')
                {
                    if (i == 1)
                    {
                        sort(space_bar.begin(), space_bar.end(), [currx, curry](pair<int, int> a, pair<int, int> b)
                             { return abs(a.first - currx) + abs(a.second - curry) < abs(b.first - currx) + abs(b.second - curry); });
                        tie(keyx, keyy) = space_bar.front();
                        ans += abs(keyx - currx) + abs(keyy - curry);
                    }
                    else
                    {
                        ans += abs(keyx - currx) + abs(keyy - curry);
                    }
                }
                else
                {
                    ans += abs(currx - prevx) + abs(curry - prevy);
                }
            }
            else
            {
                sort(space_bar.begin(), space_bar.end(), [prevx, prevy](pair<int, int> a, pair<int, int> b)
                     { return abs(a.first - prevx) + abs(a.second - prevy) < abs(b.first - prevx) + abs(b.second - prevy); });
                tie(keyx, keyy) = space_bar.front();
                ans += abs(keyx - prevx) + abs(keyy - prevy);
            }
            prev_value = current_value;
        }
        cout << (int)(ans / speed) << endl;
    }
    
    int main()
    {
        map<char, pair<int, int>> keyboard;
        insert_into_keyboard(keyboard, "1234567890", 0);
        insert_into_keyboard(keyboard, "qwertyuiop", 1);
        insert_into_keyboard(keyboard, "Casdfghjkl", 2);
        insert_into_keyboard(keyboard, "  zxcvbnm ", 3);
        int T;
        cin >> T;
    
        while (T--)
        {
            solve(keyboard);
        }
    }