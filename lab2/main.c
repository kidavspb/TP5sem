#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern unsigned char* my_enc();
extern unsigned char* my_dec();

int main() {
    register unsigned int initial_state = 0xF;
    char message[128];
    printf("Enter a string: ");
    scanf("%s", message);
    size_t size = strlen(message)+1;
    unsigned char* e = my_enc(message, initial_state, size);
    unsigned char* d = my_dec(e, initial_state, size);
    free(e);
    free(d);
}
