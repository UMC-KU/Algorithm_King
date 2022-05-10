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
vector<int> w;
vector<int> h;
vector<int> v;
vector<int> res;
int arr[100];

int main(void) {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  vector<string> white = {"WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW",
                          "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"};
  vector<string> black = {"BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB",
                          "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"};
  vector<string> v;

  int n, m;
  cin >> n >> m;
  string line;

  for (int i = 0; i < n; i++) {

    cin >> line;
    v.push_back(line);
  }

  int min = 0, res = n * m;

  for (int k = 0; k <= v.size() - 8; k++) {
    for (int h = 0; h <= line.length() - 8; h++) {
      int black_res = 0;
      int white_res = 0;
      for (int i = k; i < 8 + k; i++) {
        for (int j = h; j < 8 + h; j++) {
          for (int rep = 0; rep < 2; rep++) {
            if (rep) {
              if (v[i][j] != black[i - k][j - h]) {
                black_res++;
              }
            } else {
              if (v[i][j] != white[i - k][j - h]) {
                white_res++;
              }
            }
          }
        }
      }
      if (black_res > white_res) {
        min = white_res;
      } else {
        min = black_res;
      }
      if (min < res) {
        res = min;
      }
    }
  }
  cout << res;
  return 0;
}
