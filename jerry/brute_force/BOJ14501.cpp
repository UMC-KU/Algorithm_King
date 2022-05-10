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

int T[MAX_N];
int P[MAX_N];
int dp[MAX_N];


int main(void) {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int N; cin >> N;
	for (int i = 1; i <= N; i++) {
		cin >> T[i] >> P[i];
	}
	for (int i = 1; i <= N; i++) {
		int max_n = 0;
		for (int j = 1; j < i; j++) {
			max_n = max(max_n, dp[j]);
		}
		dp[i - 1 + T[i]] = max(dp[i - 1 + T[i]], max_n + P[i]);
		
	}
	int res = 0;
	for (int i = 1; i <= N; i++) {
		res = max(res, dp[i]);
	}
	cout << res;
}