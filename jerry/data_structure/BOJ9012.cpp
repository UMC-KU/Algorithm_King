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

  int N;
  cin >> N;

  while (N--) {
    int q_size = 0;

    string s;
    cin >> s;

    bool flag = false;
    for (int i = 0; i < s.length(); i++) {
      if (s[i] == ')') {
        if (q_size == 0) {
          flag = true;
          break;
        }
        else q_size--;
      }
      else q_size++;
    }

    if(flag || q_size != 0) cout << "NO" << endl;
    else cout << "YES" << endl;
  }
}