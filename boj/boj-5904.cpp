#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
using namespace std;
#define MAX_MOO 1000000000
int MakeMoo(string &Moo, int n) {
	string tmp = "m";
	if (Moo.size() > MAX_MOO)
		return 0;
	else {
		for (int i = 0; i < n + 2; i++) {
			tmp.push_back('o');
		}
		Moo = Moo + tmp + Moo;
		return MakeMoo(Moo, n + 1);
	}
}

int main() {
	string Moo = "moo";
	int n;
	MakeMoo(Moo, 0);
	cin >> n;
	cout << Moo.substr(n, 1) << endl;

	return 0;
}