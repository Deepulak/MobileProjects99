// Program to check
// Armstrong numbers

#include<stdio.h>

void main() {
	int temp, sum, n, k;
	scanf("%d", &n);
	temp = n;
	while (n > 0) {
		k = n % 10;
		sum += (k * k * k);
		n = n / 10;
	}
	if(temp == sum)
		printf("ARMSTRONG NUMBER\n");
	else
		printf("NOT AN ARMSTRONG NUMBER\n");
}