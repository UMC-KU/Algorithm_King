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

bool is_ok[1000];
vector<pair<int, pair<int, int>>> v;

int turn() {
  memset(is_ok, true, sizeof(is_ok));
  for (int i = 0; i <= 999; i++) {
    string tmp = to_string(i);
    if (tmp[0] == tmp[1] || tmp[0] == tmp[2] || tmp[1] == tmp[2])
      is_ok[i] = false;
    if (tmp[0] - '0' == 0 || tmp[1] - '0' == 0 || tmp[2] - '0' == 0)
      is_ok[i] = false;
  }

  for (int i = 0; i < v.size(); i++) {
    int num = v[i].first;
    int strike = v[i].second.first;
    int ball = v[i].second.second;
    string origin = to_string(num);

    for (int j = 0; j <= 999; j++) {
      int tmp_strike = 0;
      int tmp_ball = 0;
      if (is_ok[j] == true) {
        string tmp = to_string(j);
        for (int a = 0; a < 3; a++) {
          for (int b = 0; b < 3; b++) {
            if (a == b && origin[a] == tmp[b])
              tmp_strike++;
            if (a != b && origin[a] == tmp[b])
              tmp_ball++;
          }
        }
      }
      if (tmp_strike != strike || tmp_ball != ball)
        is_ok[j] = false;
    }
  }

  int ans = 0;
  for (int i = 123; i <= 999; i++) {
    if (is_ok[i] == true)
      ans++;
  }
  return ans;
}

int main(void) {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int N;
  cin >> N;

  for (int i = 1; i <= N; i++) {
    int num, strike, ball;
    cin >> num >> strike >> ball;
    v.push_back({num, {strike, ball}});
  }

  cout << turn();
}