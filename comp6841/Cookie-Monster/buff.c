#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>

#define BUFFER_SIZE 16
#define FLAG_SIZE 50
#define QUOTE_SIZE 4

char flag[FLAG_SIZE];
char quotes[QUOTE_SIZE][100] = {"NOT ENOUGH COOKIES", "I'M STILL HUNGRY", "MORE", "GRRR GIVE ME COOKIES"};

void oppsie(void) {
    char c1 = 1;
    char c2 = 1;
    char c3 = 1;
    char c4 = 1;
    char c5 = 1;
    char c6 = 1;
    char buffer[BUFFER_SIZE];
    gets(buffer);

    printf("size of buffer variable: %d", sizeof(buffer));
    printf("c1 = %c\n", c1);
    printf("c2 = %c\n", c2);
    printf("c3 = %c\n", c3);
    printf("c4 = %c\n", c4);
    printf("c5 = %c\n", c5);
    printf("c6 = %c\n", c6);

    if (c1 == 'C' && c2 == 'O' && c3 == 'O' && c4 == 'K' && c5 == 'I' && c6 == 'E') {
        printf("%s\n", flag);
        fflush(stdout);
        exit(1);
    } 
}

void cry(int counter) {
    printf("%s", quotes[counter % QUOTE_SIZE]);
    for (int i = counter*2; i > 0; i--) {
        printf("!");
    }
    printf("\n");
}

int main(int argc, char **argv){
    FILE *f = fopen("flag.txt","r");
    if (f == NULL) {
        printf("Missing flag.txt\n");
        exit(0);
    }

    fgets(flag, FLAG_SIZE, f);

    printf("HI, I'M THE COOKIE MONSTER AND I LOVE COOKIES\n");

    int counter = 0;
    while (1) {
        printf("Feed the cookie monster: ");
        fflush(stdout);
        oppsie();
        if (counter > 0) {
            cry(counter);
        }
        counter++;
    }
    return 0;
}
