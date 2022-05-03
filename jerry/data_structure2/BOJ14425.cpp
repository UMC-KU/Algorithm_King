#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <math.h>
#include <queue>
#include <set>
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

  int N, M;
  cin >> N >> M;
  // set은 중복 x하는 자료형
  set<string> s;
  string str;

  for (int i = 1; i <= N; i++) {
    cin >> str;
    s.insert(str);
  }

  int cnt = 0;
  for (int i = 1; i <= M; i++) {
    cin >> str;
    auto pos = s.find(str);
    if (pos != s.end())
      cnt++;
  }
  cout << cnt;
}