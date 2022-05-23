#include <stdlib.h>
#include <stdio.h>
#include <time.h> 
int* arr(int *A, int m, int n, int *B, int k, int p){
    int *C = (int *) malloc(m * p * sizeof(int));

    clock_t t1 = clock();

    for (int i = 0; i < m; i++){
        for (int j = 0; j < p; j++){
            C[i * m + j] = 0;
            for (int c = 0; c < k; c++){
                C[i * m + j] += A[i * m + c] * B[c * n + j];
            }
        }
    }

    clock_t t2 = clock();
    printf("%f\n", (float)(t2 - t1) / CLOCKS_PER_SEC);

    FILE* fp = fopen("mul_c", "w");

    for (int i = 0; i < m * p; i++){
        fprintf(fp, "%d ", C[i]);
    }

    return C;
}

/*
int main(){
    int A[] = {1};
    int B[] = {1, 2};
    printf("%d", arr(A, 1, 1, B, 1, 2)[1]);
    return 0;
}
*/
