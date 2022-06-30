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

int dy[] = {-1, -1, 0, 1, 1, 1, 0, -1}, dx[] = {0, 1, 1, 1, 0, -1, -1, -1};

int main(void) {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int N, M, K;
  cin >> N >> M >> K;

  vector<pair<pair<int, int>, tuple<int, int, int>>>
      v[50 + 5][50 + 5]; // 확산 후 파이어볼
  vector<pair<pair<int, int>, tuple<int, int, int>>>
      fire_ball; // 확산 전 파이어볼

  for (int i = 1; i <= M; i++) {
    int y, x, m, d, s;
    cin >> y >> x >> m >> s >> d;
    // v[y][x].push_back({{y, x}, {m, s, d}});
    fire_ball.push_back({{y, x}, {m, s, d}});
  }

  for (int i = 1; i <= K; i++) {

    for (int h = 1; h <= N; h++) {
      for (int k = 1; k <= N; k++) {
        v[h][k].clear();
      }
    }

    int size = fire_ball.size();
    for (int j = 0; j < size; j++) {
      int y = fire_ball[j].first.first;
      int x = fire_ball[j].first.second;
      int m = get<0>(fire_ball[j].second);
      int s = get<1>(fire_ball[j].second);
      int d = get<2>(fire_ball[j].second);

      // 격자 넘어가면
      int ny, nx;
      ny = y + dy[d] * s % N;
      nx = x + dx[d] * s % N;
      if (ny > N)
        ny -= N;
      if (ny < 1)
        ny += N;
      if (nx > N)
        nx -= N;
      if (nx < 1)
        nx += N;

      v[ny][nx].push_back({{ny, nx}, {m, s, d}});
      // cout << ny << " " << nx << " " << m << " " << s << " " << d << endl;
      // fire_ball[j].first.first = ny;
      // fire_ball[j].first.second = nx;
    }

    vector<pair<pair<int, int>, tuple<int, int, int>>> temp; // 합쳐진 파이어볼

    for (int h = 1; h <= N; h++) {
      for (int k = 1; k <= N; k++) {
        if (v[h][k].size() == 0)
          continue;
        else if (v[h][k].size() == 1) {
          temp.push_back({{h, k},
                          {get<0>(v[h][k][0].second), get<1>(v[h][k][0].second),
                           get<2>(v[h][k][0].second)}});
        } else {
          int t_m = 0, t_s = 0;
          bool even = true;
          bool odd = true;
          for (int g = 0; g < v[h][k].size(); g++) {
            t_m += get<0>(v[h][k][g].second);
            t_s += get<1>(v[h][k][g].second);

            // 방향이 모두 짝, 홀인 경우
            if (get<2>(v[h][k][g].second) % 2 != 0)
              even = false;
            if (get<2>(v[h][k][g].second) % 2 == 0)
              odd = false;
          }

          t_m /= 5;
          t_s /= v[h][k].size();

          if (t_m != 0) {
            if (even == true || odd == true) {
              temp.push_back({{h, k}, {t_m, t_s, 0}});
              temp.push_back({{h, k}, {t_m, t_s, 2}});
              temp.push_back({{h, k}, {t_m, t_s, 4}});
              temp.push_back({{h, k}, {t_m, t_s, 6}});

            } else {
              temp.push_back({{h, k}, {t_m, t_s, 1}});
              temp.push_back({{h, k}, {t_m, t_s, 3}});
              temp.push_back({{h, k}, {t_m, t_s, 5}});
              temp.push_back({{h, k}, {t_m, t_s, 7}});
            }
          }
        }
      }
    }
    fire_ball = temp;
  }
  int ans = 0;
  for (int i = 0; i < fire_ball.size(); i++) {
    ans += get<0>(fire_ball[i].second);
  }
  cout << ans;
}