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
#define MAX_N 50 + 5
#define endl "\n"
#define INF 2147483647
typedef long long ll;
// typedef pair<int, int> pii;
using namespace std;

int Map[50 + 5][50 + 5];
bool check[50 + 5][50 + 5];
int dy[] = {0, 1, 0, -1}, dx[] = {1, 0, -1, 0};
int N, L, R;

bool bfs(int now_y, int now_x) {
  queue<pair<int, int>> q;
  q.push({now_y, now_x});
  check[now_y][now_x] = true;

  bool flag = false;
  while (!q.empty()) {
    int y = q.front().first;
    int x = q.front().second;
    q.pop();

    for (int i = 0; i < 4; i++) {
      int ny = y + dy[i];
      int nx = x + dx[i];
      if (ny < 1 || ny > N || nx < 1 || nx > N)
        continue;
      if (check[ny][nx] || abs(Map[ny][nx] - Map[y][x]) < L ||
          abs(Map[ny][nx] - Map[y][x]) > R)
        continue;
      flag = true;
      q.push({ny, nx});
      check[ny][nx] = true;
    }
  }
  return flag;
}

int main(void) {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  cin >> N >> L >> R;
  
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      cin >> Map[i][j];
    }
  }

  int t = 0;
  while (true) {
    int n = 0;
    memset(check, false, sizeof(check));
    bool mv = false;
    for (int i = 1; i <= N; i++) {
      for (int j = 1; j <= N; j++) {
        if (check[i][j] == false) {
          mv = mv || bfs(i, j);
        }
      }
    }
    if(mv == false) break;
    t++;
  }
  cout << t;
}
