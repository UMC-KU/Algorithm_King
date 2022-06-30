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

int arr[20 + 5][20 + 5];
int shark_size = 2;
int dy[] = {-1, 0, 0, 1}, dx[] = {0, -1, 1, 0};
int N;
int res;
int num;
int shark_y, shark_x;
pair<int,int> bfs(pair<int, int> now);

int main(void) {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  cin >> N;
  
  // 전체 공간의 상태 입력
  // 0 : 빈칸, 9 : 아기상어의 위치
  // 1, 2, 3, 4, 5, 6 : 칸에 있는 물고기의 크기

  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      cin >> arr[i][j];
      if (arr[i][j] == 9) {
        shark_y = i;
        shark_x = j;
        arr[i][j] = 0;
      }
    }
  }

  while(1){
    bfs({shark_y,shark_x});
  }
  
  

  return 0;
}
pair<int,int> bfs(pair<int, int> now) {
  queue<pair<pair<int, int>, int> q; // 물고기 y좌표, x좌표, 시간, 잡아먹은 물고기 수
  q.push({{now.first, now.second}, {0, 0}});
  bool visited[20 + 5][20 + 5];
  memset(visited,false,sizeof(visited));
  visited[now.first][now.second] = true;

  while (!q.empty()) {
    int y = q.front().first.first;
    int x = q.front().first.second;
    int dist = q.front().second.first;

    q.pop();

    int min_num = INF;
    for (int i = 1; i <= N; i++) {
      for (int j = 1; j <= N; j++) {
        if (arr[i][j] < min_num && arr[i][j] != 0) {
          min_num = arr[i][j];
        }
      }
    }

    cout << "x : " << x << " y : " << y << " time : " << time << " num : " << num;
    cout << " min num : " << min_num << " shark_size : " << shark_size << endl;
    if (min_num >= shark_size) {
      cout << time;
      break;
    }

    for (int i = 0; i < 4; i++) {
      int ny = y + dy[i];
      int nx = x + dx[i];
      if (ny < 1 || ny > N || nx < 1 || nx > N || arr[ny][nx] > shark_size || visited[ny][nx] == true)
        continue; // 왼쪽 위가 먼저 가도록!
      if (arr[ny][nx] < shark_size && arr[ny][nx] != 0) {
        arr[ny][nx] = 0;
        while (!q.empty())
          q.pop();
        visited[ny][nx] = true;
        q.push({{ny, nx}, abs(ny-y) + abs(nx-x)});
      }
      if (arr[ny][nx] == shark_size || arr[ny][nx] == 0)
        q.push({{ny, nx}, {time + 1, num}});
      // visited[ny][nx] = true;
    }
  }
}
