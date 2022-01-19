#include <stdio.h>
#include <time.h>

int main() {
    unsigned int a, x;
    unsigned int maior_seq = 0, soma_seq = 0, valor_maior_seq, cont;
    double media_seq;

    clock_t begin = clock();

    for(a = 1 ; a < 65535 ; a++){
        x = a;
        cont = 1;

        while(x > 1){
            if((x & 1) == 0){
                x >>=1;
            } else{
                x = 3 * x + 1;
            }
            cont++;
        }

        if(cont > maior_seq){
            maior_seq = cont;
            valor_maior_seq = a;
        }
        soma_seq += cont;
    }

    clock_t end = clock();

    media_seq = (double)(soma_seq)/65535; 

    //printf("Unsigned int size: %li bytes\n", sizeof(unsigned int));
    //printf("Unsigned short int size: %li bytes\n", sizeof(unsigned short int));
    printf("Maior sequencia encontrada: %u\n", maior_seq);
    printf("Valor de a para a maior sequencia encontrada: %u\n", valor_maior_seq);
    printf("Media dos tamanhos das sequencias: %lf\n", media_seq);
    printf("Tempo de execucao: %lf segundos", (double)(end - begin) / CLOCKS_PER_SEC);
    
    return 0;
}