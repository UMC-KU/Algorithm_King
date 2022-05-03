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

  priority_queue<int> pq;
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      int x;
      cin >> x;
      pq.push(-x);
      if (pq.size() > N)
        pq.pop();
    }
  }
  cout << -pq.top();
}