#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	char array[5][15] = {NULL};
	int i, j;

	// ���ڿ� �迭 �ޱ�
	for (i = 0; i < 5; i++)
	{
		scanf("%s", array + i);
	}
	// ����Ʈ
	for (i = 0; i < 15; i++)
	{
		for (j = 0; j < 5; j++)
		{
			if (array[j][i] == NULL)
				continue;
			else
			{
				if ((int)array[j][i] > 9)
					printf("%c", array[j][i]);
				else
					printf("%d", array[j][i]);
			}
		}
	}
	printf("\n");
	return 0;
}