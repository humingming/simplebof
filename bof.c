#include<stdio.h>

void print(char * str) {
	char buf[200];
	strcpy(buf, str);
	printf("%s\n");
}

int main(int argc, char * argv[])
{
	if(argc == 2) {
		print(argv[1]);
	}
	return 0;
}

