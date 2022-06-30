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

int A[100 + 5][100 + 5];
int N, M;
vector<pair<int, int>> v;
vector<pair<int, int>> imsi;

bool checkDiagonal(pair<int, int> p) {
  if (p.first < 1 || p.first > N || p.second < 1 || p.second > N) {
    return false;
  } else if (A[p.first][p.second] > 0) {
    return true;
  }
  return false;
}

pair<int, int> moving(pair<int, int> p) {
  if (p.first > N) {
    // p.first = p.first % N;
    p.first = (p.first - 1) % N + 1;
  } else if (p.first < 1) {
    // p.first = (p.first % N) + N;
    p.first = N - ((-p.first) % N);
  }

  if (p.second > N) {
    // p.second = p.second % N;
    p.second = (p.second - 1) % N + 1;
  } else if (p.second < 1) {
    // p.second = (p.second % N) + N;
    p.second = N - ((-p.second) % N);
  }
  /*p.first = (p.first - 1) % N + 1;
  p.second = (p.second - 1) % N + 1;*/

  A[p.first][p.second]++;
  imsi.push_back({p.first, p.second});
  // cout << "moving : " << p.first << " " << p.second << endl;
  return {p.first, p.second};
}

int main(void) {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  cin >> N >> M;

  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      cin >> A[i][j];
    }
  }

  pair<int, int> b1, b2, b3, b4;
  b1 = {N, 1};
  b2 = {N, 2};
  b3 = {N - 1, 1};
  b4 = {N - 1, 2};

  v.push_back(b1);
  v.push_back(b2);
  v.push_back(b3);
  v.push_back(b4);
  int d, s;
  vector<pair<int, int>> temp;

  for (int i = 1; i <= M; i++) {
    cin >> d >> s;

    if (d == 1) {
      for (int j = 0; j < v.size(); j++) {
        //cout << v[j].first << " " << v[j].second << endl;
        v[j] = moving({v[j].first, v[j].second - s});
        //cout << v[j].first << " " << v[j].second << endl;
      }
    } else if (d == 2) {
      for (int j = 0; j < v.size(); j++) {
        v[j] = moving({v[j].first - s, v[j].second - s});
      }
    } else if (d == 3) {
      for (int j = 0; j < v.size(); j++) {
        v[j] = moving({v[j].first - s, v[j].second});
      }
    } else if (d == 4) {
      for (int j = 0; j < v.size(); j++) {
        v[j] = moving({v[j].first - s, v[j].second + s});
      }
    } else if (d == 5) {
      for (int j = 0; j < v.size(); j++) {
        v[j] = moving({v[j].first, v[j].second + s});
      }
    } else if (d == 6) {
      for (int j = 0; j < v.size(); j++) {
        v[j] = moving({v[j].first + s, v[j].second + s});
      }
    } else if (d == 7) {
      for (int j = 0; j < v.size(); j++) {
        v[j] = moving({v[j].first + s, v[j].second});
      }
    } else if (d == 8) {
      for (int j = 0; j < v.size(); j++) {
        v[j] = moving({v[j].first + s, v[j].second - s});
      }
    }

    for (int j = 0; j < v.size(); j++) {
      if (checkDiagonal({v[j].first - 1, v[j].second - 1}))
        A[v[j].first][v[j].second]++;
      if (checkDiagonal({v[j].first + 1, v[j].second - 1}))
        A[v[j].first][v[j].second]++;
      if (checkDiagonal({v[j].first + 1, v[j].second + 1}))
        A[v[j].first][v[j].second]++;
      if (checkDiagonal({v[j].first - 1, v[j].second + 1}))
        A[v[j].first][v[j].second]++;
    }

    for (int j = 1; j <= N; j++) {
      for (int k = 1; k <= N; k++) {
        bool flag = false;
        for (int h = 0; h < imsi.size(); h++) {
          if (j == imsi[h].first && k == imsi[h].second)
            flag = true;
        }
        if (!flag) {
          if (A[j][k] >= 2) {
            temp.push_back({j, k});
            A[j][k] -= 2;
          }
        }
      }
    }

    v.clear();
    for (int j = 0; j < temp.size(); j++) {
      // cout << "temp : " << temp[j].first << " " << temp[j].second << endl;
      v.push_back({temp[j].first, temp[j].second});
    }
    temp.clear();
    imsi.clear();
    // for (int i = 1; i <= N; i++) {
    //   for (int j = 1; j <= N; j++) {
    //     cout << A[i][j] << " ";
    //   }
    //   cout << endl;
    // }
  }

  int result = 0;
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      result += A[i][j];
    }
  }
  cout << result;
}