#include <stdio.h>
#include <unistd.h>

char string[100];

void exec_str()
{
    setgid(1001);
    setuid(1001);
    system(string);
}

void add_bin_str(int arg1, int arg2)
{
    if (arg1 == 0xdeadc0de && arg2 == 0x0badfeed)
    {
        strcat(string, "/bin");
    }
}

void add_sh_str(int arg1)
{

    if (arg1 == 0xbaaaaaad)
    {

        strcat(string, "/sh");
    }
}

void whoami()
{
    setuid(1001);
    system("/usr/bin/whoami");
}

void parser(char *string)
{

    char buffer[100];
    if (strncmp(string, "whoami", strlen("whoami")) == 0) {

        whoami();
    }
    else
    {
        strcpy(buffer, string);
        printf("Please use a valid command\n");


    }
}

int main(int argc, char **argv)
{

    printf("Hello and welcome to Rob's admin program!\n");
    printf("This program will use my permissions so that everyone can manage this server\n");
    string[0] = 0;

    if (argc > 1)
    {

        parser(argv[1]);
    }

    else
    {

        printf("This program needs an command line argument\n");
    }

    return 0;
}
