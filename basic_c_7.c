// Program to check 
// a Prime number
#include<stdio.h>

void main() {
	int n, i;
	scanf("%d", &n);
	bool flag = 1;
	for(i = 0; i < n; i++) {
		if(n % i == 0) {
			flag = 0;
			break;
		}
		if(flag == 0)
			printf("NOT A PRIME NUMBER\n");
		else
			printf("PRIME NUMBER\n");
	}
}