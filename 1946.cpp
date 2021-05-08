#include <stdio.h>
#include <stdlib.h>

int t[100001] = { 0, };

int main(void)
{
	int numCount, testCase;
	int min0;
	int first, second;


	scanf("%d", &testCase);

	for (int i = 0; i < testCase; i++)
	{
		int count = 1;
		scanf("%d", &numCount);

		for (int j = 0; j < numCount; j++)
		{

			scanf("%d %d", &first, &second);
			t[first] = second;
		}



		count = 0;
		min0 = 1000001;
		for (int j = 0; j < 100001; j++)
		{
			if (t[j] != 0 && t[j]<min0)
			{
				min0 = t[j];
				count++;
			}
		}

		printf("%d\n", count);
	}

	return 0;
}
