// Program to print sum of
// digits of a number

#include<stdio.h>

int main() {
	int sum, n;
	scanf("%d", &n);
	while(n>0) {
		sum += n % 10;
		n = n / 10;
	}
	printf("sum of digits = %d", sum);
	return 0;
}