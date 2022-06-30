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

int arr[MAX_N][MAX_N];
int temp[MAX_N][MAX_N];
int R, C, T;
int dy[] = {-1, 0, 1, 0}, dx[] = {0, 1, 0, -1};
int dy_up[] = {0, -1, 0, 1}, dx_up[] = {1, 0, -1, 0};
int dy_down[] = {0, 1, 0, -1}, dx_down[] = {1, 0, -1, 0};

pair<int, int> air_cleaner; // 공기청정기의 위치 (i+1,j),(i,j)

void spread() { // 미세먼지의 확산
  for (int i = 1; i <= R; i++) {
    for (int j = 1; j <= C; j++) {
      int num = 0;
      for (int k = 0; k < 4; k++) {
        int ny = i + dy[k];
        int nx = i + dx[k];
        if (ny < 1 || ny > R || nx < 1 || nx > C)
          continue;
        if (arr[ny][nx] == -1)
          continue;
        temp[ny][nx] += arr[i][j] / 5;
        num++;
      }
      arr[i][j] = arr[i][j] - (arr[i][j] / 5) * num;
    }
  }
}

void working_cleaner(pair<int, int> start, int sign) { // 공기청정기 작동
  bool visited[MAX_N][MAX_N];
  memset(visited, false, sizeof(visited));
  queue<pair<int, int>> q;
  q.push({start.first, start.second});
  int temp = 0;
  int imsi = 0;
  while (!q.empty()) {
    int y = q.front().first;
    int x = q.front().second;
    q.pop();

    if (sign == 0) {
      for (int i = 0; i < 4; i++) {
        int ny = y + dy_up[i];
        int nx = x + dx_up[i];
        if (ny < 1 || ny > R || nx < 1 || nx > C || visited[ny][nx] == true)
          continue;
        if (arr[ny][nx] == -1)
          break;
        temp = arr[ny][nx];
        arr[ny][nx] = imsi;
        imsi = temp;
        visited[ny][nx] = true;
        q.push({ny, nx});
        break;
      }
    } else if (sign == -1) {
      for (int i = 0; i < 4; i++) {
        int ny = y + dy_down[i];
        int nx = x + dx_down[i];
        if (ny < 1 || ny > R || nx < 1 || nx > C)
          continue;
        if (arr[ny][nx] == -1)
          break;
        temp = arr[ny][nx];
        arr[ny][nx] = imsi;
        imsi = temp;
        visited[ny][nx] = true;
        q.push({ny, nx});
      }
    }
  }
}

int main(void) {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  cin >> R >> C >> T;

  for (int i = 1; i <= R; i++) {
    for (int j = 1; j <= C; j++) {
      cin >> arr[i][j];
      if (arr[i][j] == -1) {
        air_cleaner = {i, j};
      }
    }
  }

  int time = 0;
  while (time < T) {
    time++;
    memset(temp, 0, sizeof(temp));
    spread();

    for (int i = 1; i <= R; i++) {
      for (int j = 1; j <= C; j++) {
        arr[i][j] = temp[i][j] + arr[i][j];
      }
    }

    for (int i = 1; i <= R; i++) {
      for (int j = 1; j <= C; j++) {
        cout << arr[i][j] << " ";
      }
      cout << endl;
    }

    working_cleaner({air_cleaner.first - 1, air_cleaner.second},
                    0); // 위쪽 공기청정기
    working_cleaner({air_cleaner.first, air_cleaner.second},
                    1); // 아래쪽 공기청정기

    // for (int i = 1; i <= R; i++) {
    //   for (int j = 1; j <= C; j++) {
    //     cout << arr[i][j] << " ";
    //   }
    //   cout << endl;
    // }
  }

  int result = 0;
  for (int i = 1; i <= R; i++) {
    for (int j = 1; j <= C; j++) {
      if (arr[i][j] != -1) {
        result += arr[i][j];
      }
    }
  }
  cout << result;

  return 0;
}
