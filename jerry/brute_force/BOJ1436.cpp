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
int cnt[10000 + 5];

int main(void) {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int N;
  cin >> N;
  int idx = 1;
  for (int i = 666; i <= 10000666; i++) {
    string str = to_string(i);

    if (str.find("666") != std::string::npos) {
      cnt[idx] = stoi(str);
      idx++;
    }
    if (idx > N)
      break;
  }
  cout << cnt[N];
}