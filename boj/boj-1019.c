#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int i, n;
	int num[10] = { 0 };

	scanf("%d", &n);

	for (i = 1; i < n + 1; i++) {
		int tmp = i;
		while (tmp > 9) {
			num[tmp % 10]++;
			tmp /= 10;
		}
		num[tmp]++;
	}

	for (i = 0; i < 10; i++) {
		printf("%d ", num[i]);
	}

	return 0;
}