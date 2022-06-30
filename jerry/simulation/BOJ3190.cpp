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

int arr[MAX_N][MAX_N];
vector<pair<int, int>> bam; // 뱀이 있는 곳
queue<pair<int, char>> q;   // 사과가 있는 곳
void gameon(pair<int, int> p, char dir, int time);
int dx[] = {1, 0, -1, 0}, dy[] = {0, 1, 0, -1};
int N;
int h = 0;

int main(void) {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  cin >> N;
  int K;
  cin >> K;
  for (int i = 1; i <= K; i++) {
    int a, b;
    cin >> a >> b;
    arr[a][b] = 1;
  }
  int L;
  cin >> L;
  for (int i = 1; i <= L; i++) {
    int a;
    char b;
    cin >> a >> b;
    q.push({a, b});
  }
  bam.push_back({1, 1});
  /*vector<int>v = { 1,2,3 };
  cout << v.size() << " ";
  v.erase(v.begin());
  cout << v.size() << " ";*/

  gameon({1, 1}, 'r', 0);
}

void gameon(pair<int, int> p, char dir, int time) {
  time = time + 1;
  int d = 0;

  if (dir == 'r')
    d = 0;
  else if (dir == 'u')
    d = 1;
  else if (dir == 'l')
    d = 2;
  else if (dir == 't')
    d = 3;

  int now_x = p.second;
  int now_y = p.first;
  int nex_x = now_x + dx[d];
  int nex_y = now_y + dy[d];

  // 벽에 부딛히면
  if (nex_x < 1 || nex_x > N || nex_y < 1 || nex_y > N) {
    cout << time;
    return;
  }

  //뱀의 몸과 만나면
  for (int i = 0; i < bam.size(); i++) {
    if (bam[i].first == nex_y && bam[i].second == nex_x) {
      cout << time;
      return;
    }
  }

  if (!q.empty()) {
    if (time == q.front().first) {
      char turn = q.front().second;
      q.pop();
      if (turn == 'L') {
        if (dir == 'r')
          dir = 't';
        else if (dir == 'u')
          dir = 'r';
        else if (dir == 'l')
          dir = 'u';
        else if (dir == 't')
          dir = 'l';
      } else {
        if (dir == 'r')
          dir = 'u';
        else if (dir == 'u')
          dir = 'l';
        else if (dir == 'l')
          dir = 't';
        else if (dir == 't')
          dir = 'r';
      }
    }
  }

  //다음 자리에 사과가 있으면
  if (arr[nex_y][nex_x]) {
    arr[nex_y][nex_x] = 0;
    bam.push_back({nex_y, nex_x});
    gameon({nex_y, nex_x}, dir, time);
  } else {
    bam.push_back({nex_y, nex_x});
    bam.erase(bam.begin());
    gameon({nex_y, nex_x}, dir, time);
  }
}
