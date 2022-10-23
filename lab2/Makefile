all: main.o asm.o
	gcc -ggdb main.o asm.o -o result
	rm *.o

main.o: main.c
	gcc -ggdb main.c -c -o main.o

asm.o: asm.s
	as -g asm.s -o asm.o

clean:
	rm *.o
	rm result
