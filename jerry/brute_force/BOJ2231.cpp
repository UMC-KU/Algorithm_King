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

  int N, M;
  cin >> N >> M;

  vector<string> v;
  string s;
  for (int i = 0; i < N; i++) {
    cin >> s;
    v.push_back(s);
  }

  vector<string> str = {"A", "C", "G", "T"};

  int res = 0;
  string res_str = "";
  for (int i = 0; i < M; i++) {
    int arr[] = {0, 0, 0, 0};
    for (int j = 0; j < v.size(); j++) {
      if (v[j][i] == 'A') {
          arr[0]++;
        } else if (v[j][i] == 'C') {
          arr[1]++;
        } else if (v[j][i] == 'G') {
          arr[2]++;
        } else if (v[j][i] == 'T') {
          arr[3]++;
        }
    }
    int maxVal = 0;
    string sub = "";
    for (int k = 0; k < 4; k++) {
      if (maxVal < arr[k]) {
        maxVal = max(maxVal, arr[k]);
        sub = str[k];
      }
    }
    res += (v.size() - maxVal);
    res_str += sub;
  }
  cout << res_str << endl << res << endl;
}