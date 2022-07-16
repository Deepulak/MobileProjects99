// Program to find a Factorial
// of Entered Number

#include<stdio.h>

void main() {
	int n, fact;
	printf("Enter the NO: ");
	scanf("%d", &n);
	fact = 1;
	while(n>0) {
		fact = fact * n;
		n = n - 1;
	}
	printf("Factorial of %d is %d", n, fact);
}