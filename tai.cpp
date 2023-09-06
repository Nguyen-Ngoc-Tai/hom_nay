#include<stdio.h>
#include<conio.h>

int main()
{
    int i, n;
    long S;
    S = 0;
    i = 1;
    printf("\nNhap n: ");
    scanf("%d", &n);

    while(i <= n)
    {
        S = S + i;
        i++;
    }
    printf("\nTong 1 + 2 + ... + %d la %ld: ", n, S);
    printf("Them cai ni vo nua ca bi lon");
    printf("Thek hoios");
    getch();
    return 0;
}