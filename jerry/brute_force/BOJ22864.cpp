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

  int A, B, C, M;
  cin >> A >> B >> C >> M;

  int prio = 0;
  int res = 0;
  int day = 24;
  while (day--) {
    if (prio + A <= M) {
      prio += A;
      res += B;
    } else {
      prio -= C;
      if (prio < 0)
        prio = 0;
    }
  }
  cout << res;
}