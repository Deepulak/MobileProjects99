// Program to print Fibonacci series
#include<stdio.h>

void main() {
	int t1, t2, t3, n;
	scanf("%d", n);
	t1 = 0;
	t2 = 1;
	while(n--) {
		t3 = t1 + t2;
		printf("%d", t1);
		t1 = t2;
		t2 = t3;
	}
return 0;
}