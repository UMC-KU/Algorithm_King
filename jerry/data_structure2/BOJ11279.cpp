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

  // map<key,value>: key와 value를 pair 형태로 선언합니다.
  // map은 key값을 기준으로 오름차순 정렬되어 있습니다.
  string str;
  float cnt = 0;
  map<string, int> m;
  while (getline(cin, str)) {
    cnt++;
    if (m.find(str) != m.end()) {
      m[str] += 1;
    } else
      m[str] = 1;
  }
  cout << fixed;
  cout.precision(4);
  for (auto it = m.begin(); it != m.end(); it++) {
    float val = (it->second / cnt) * 100;
    cout << it->first << " ";
    cout << val << endl;
  }
}