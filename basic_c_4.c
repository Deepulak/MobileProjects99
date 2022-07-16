// Program to reverse a number

#include <stdio.h>

int main() {
	int n, rev, dig;
	scanf("%d", &n);
	rev = 0;
	while(n>0){
		dig = n % 10;
		rev = rev * 10 + dig;
		n = n / 10;
	}
	printf("%d", rev);
	return 0;
}