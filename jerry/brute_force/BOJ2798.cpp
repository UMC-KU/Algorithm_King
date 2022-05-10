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

int main(void) {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  const int r = 3;

  int N, M;
  cin >> N >> M;

  vector<int> v;
  for (int i = 1; i <= N; i++) {
    int x;
    cin >> x;
    v.push_back(x);
  }
  vector<bool> temp(v.size(), false);

  for (int i = 0; i < r; i++) {
    temp[i] = true;
  }

  int ans = 0;
  do{
    int res = 0;
    for(int i = 0;i<v.size();i++){
      if(temp[i])
        res += v[i];
    }
    if(res <= M && res >= ans){
      ans = res;
    }
  }while(prev_permutation(temp.begin(),temp.end()));

  cout << ans;
}