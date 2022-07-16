// Program to check a 
// Palindrome number

#include<stdio.h>
int main() {
	int n, rev, dig, temp;
	scanf("%d", &n);
	rev = 0;
	temp = n;
	while(n > 0) {
		dig = n % 10;
		rev = rev * 10 + dig;
		n = n / 10;
	}
	if(rev == temp)
		printf("PALINDROME NUMBER\n");
	else
		printf("NOT A PALINDROME NUMBER\n");
	return 0;

}