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

  int x, sum = 0;
  vector<int> v;
	for (int i = 1; i <= 9; i++) {
		cin >> x;
		v.push_back(x);
		sum += x;
	}
	bool check = false;
	int not_sum = sum - 100;
	for (int i = 0; i < 8; i++) {
		for (int j = i + 1; j < 9; j++) {
			if (v[i] + v[j] == not_sum) {
				v[i] = 0;
				v[j] = 0;
				sort(v.begin(), v.end());
				for (int k = 2; k < 9; k++) {
					cout << v[k] << endl;
				}
				check = true;
			}
			if (check) {
				break;
			}
		}
		if (check) {
			break;
		}
	}
}

