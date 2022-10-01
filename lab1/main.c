#include <stdio.h>

static unsigned int S = 0xF;

int LFSR_Fibonacci (void) {
    S = ((((S >> 1) ^ S ) & 0x1 ) << 3) | (S >> 1); // 
    return S & 0x1;
}

int main() {
    register unsigned int initial_state = 0xF;
    printf("-----Шифруем-----\n");
    S = initial_state;
    char message[] = "Hello!";
    unsigned char enc[256];
    int a[256];
    int size = sizeof(message)/sizeof(char) -1;
    for (int i = 0; i < size; i++) {
        unsigned int tmp = 0;
        for (int j = 7; j >=0; j--) {
            int genbit = LFSR_Fibonacci() & 0x1;
            tmp = (tmp << 1) | (genbit ^ ((message[i] >> j) & 0x01));
            printf("%x = %x ^ (%x >> %d) & 0x01)\n", tmp, genbit, message[i], j);
        }
        enc[i] = tmp;
        printf("%x (%c) -> %x (%c)\n", message[i], message[i], enc[i], enc[i]);
    }
    enc[size-1] = '\0';
    printf("%s -> %s\n\n\n", message, enc);
    
    printf("-----Расшифровываем-----\n");
    S = initial_state;
    char plain[256];
    for (int i = 0; i < size; i++) {
        unsigned int tmp = 0;
        for (int j = 7; j >=0; j--) {
            int genbit = LFSR_Fibonacci() & 0x1;
            tmp = (tmp << 1) | (genbit ^ ((enc[i] >> j) & 0x01));
            printf("%x = %x ^ (%x >> %d) & 0x01)\n", tmp, genbit, enc[i], j);
        }
        plain[i] = tmp;
        printf("%x (%c) -> %x (%c)\n", enc[i], enc[i], plain[i], plain[i]);
    }
    plain[size-1] = '\0';
    printf("%s -> %s\n\n\n", enc, plain);
}
