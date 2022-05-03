#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <math.h>
#include <queue>
#include <string>
#include <tuple>
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

  deque<pair<int, int>> dq;
  vector<int> res;
  int N;
  cin >> N;

  for (int i = 1; i <= N; i++) {
    int x;
    cin >> x;
    dq.push_back({i, x});
  }

  res.push_back(1);
  int t = dq.front().second;
  dq.pop_front();
  while (!dq.empty()) {
    if (t >= 0) {
      int dq_1, dq_2;
      for (int i = 1; i < t; i++) {
        dq_1 = dq.front().first;
        dq_2 = dq.front().second;
        dq.pop_front();
        dq.push_back({dq_1, dq_2});
      }
      dq_1 = dq.front().first;
      dq_2 = dq.front().second;
      dq.pop_front();
      res.push_back(dq_1);
      t = dq_2;
    } else {
      int dq_1, dq_2;
      for (int i = 1; i < -t; i++) {
        dq_1 = dq.back().first;
        dq_2 = dq.back().second;
        dq.pop_back();
        dq.push_front({dq_1, dq_2});
      }
      dq_1 = dq.back().first;
      dq_2 = dq.back().second;
      dq.pop_back();
      res.push_back(dq_1);
      t = dq_2;
    }
  }
  for (int i = 0; i < res.size(); i++) {
    cout << res[i] << " ";
  }
}