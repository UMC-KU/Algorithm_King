#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <math.h>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <unordered_map>
#include <vector>
#define MAX_N 1000 + 5
#define endl "\n"
#define INF 2147483647
typedef long long ll;
// typedef pair<int, int> pii;
using namespace std;

int main(void) {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int N;
  cin >> N;
  map<int, int> m;
  priority_queue<pair<int, int>> hard;
  priority_queue<pair<int, int>> easy;

  int a, b;
  for (int i = 1; i <= N; i++) {
    cin >> a >> b;
    m.insert({a, b});
    hard.push({b, a});
    easy.push({-b, -a});
  }

  cin >> N;
  string str;
  vector<string> words;
  string stringBuffer;
  words.clear();
  for (int i = 1; i <= N; i++) {
    getline(cin, str);
    istringstream ss(str);
    // ss.str();
    while (ss >> stringBuffer) {
      words.push_back(stringBuffer);
      cout << stringBuffer << " ";
    }
    cout << endl;

    /* if (words[0] == "add") {
         m.insert({ stoi(words[1]), stoi(words[2]) });
     }
     else if (words[0] == "solved") {
         m.erase(stoi(words[1]));
     }
     else if (words[0] == "recommend") {
         if (stoi(words[1]) == 1) {
             cout << hard.top().second << endl;
         }
         else {
             cout << -easy.top().second << endl;
         }
     }*/
    words.clear();
  }
}