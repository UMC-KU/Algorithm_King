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

  unordered_map<int, string> map1;
  unordered_map<string, int> map2;
  string s;
  for (int i = 1; i <= N; i++) {
    cin >> s;
    map1[i] = s;
    map2[s] = i;
  }

  for (int i = 1; i <= M; i++) {
    string str;
    cin >> str;

    if (str[0] - '0' >= 1 && str[0]- '0' <= 9) {
      cout << map1[stoi(str)] << endl;
    } else
      cout << map2[str] << endl;
  }
}