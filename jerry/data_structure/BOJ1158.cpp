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

  int N, K;
  cin >> N >> K;

  queue<int> q;

  for (int i = 1; i <= N; i++) {
    q.push(i);
  }

  vector<int> v;

  while (!q.empty()) {
    for (int i = 1; i < K; i++) {
      int n = q.front();
      q.pop();
      q.push(n);
    }
    int now = q.front();
    q.pop();
    v.push_back(now);
  }

  cout << "<";
  for (int i = 0; i < v.size() - 1; i++) {
    cout << v[i] << ", ";
  }
  cout << v[N - 1] << ">";
}