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
vector<int> tree[50 + 5];
int rootNode;
int leafNode;
int delNode;

int dfs(int node, int ded) {
  int child = 0;

  for (int i = 0; i < tree[node].size(); i++) {
    if (tree[node][i] == ded)
      continue;
    child += dfs(tree[node][i], ded);
  }

  if (child != 0)
    return child;
  else
    return 1;
}

int main(void) {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int N;
  cin >> N;

  int x;
  for (int i = 0; i < N; i++) {
    cin >> x;
    if (x == -1) {
      rootNode = i;
    } else {
      tree[x].push_back(i);
    }
  }

  cin >> delNode;

  if (delNode == rootNode) {
    cout << "0";
  } else {
    cout << dfs(rootNode, delNode);
  }
  return 0;
}
