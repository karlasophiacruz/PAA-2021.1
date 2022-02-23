#include <stdio.h>
#include <time.h>
 

const int N = 8;
int moveX[] = { 2, 1, -1, -2, -2, -1, 1, 2 };
int moveY[] = { 1, 2, 2, 1, -1, -2, -2, -1 };
 

int not_visited(int x, int y, int board[N][N]) {
    return x >= 0 && x < N && y >= 0 && y < N && board[x][y] == -1;
}
 

int horse_path(int x, int y, int moveN, int board[N][N]) {
    int i, proxX, proxY;

    if (moveN == N * N) {
        board[x][y] = N * N;
        return 1;
    }
 
    for (i = 0 ; i < 8 ; i++) {
        proxX = x + moveX[i];
        proxY = y + moveY[i];
 
        if (not_visited(proxX, proxY, board)) {
            board[x][y] = moveN;
 
            if (horse_path(proxX, proxY, moveN + 1, board)) {
                return 1;
            }
 
            board[proxX][proxY] = -1;
        }
    }
 
    return 0;
}


void main() {
    int board[N][N], i, j, solution;
    clock_t t;
 
    for(i = 0 ; i < N ; i++) {
        for(j = 0; j < N; j++) {
            board[i][j] = -1;
        }
    }
 
    board[0][0] = 0;
    
    t = clock();
    solution = horse_path(0, 0, 1, board);
    t = clock() - t;

    if (!solution) {
        printf("No solution!");
        return;
    }
 
    for(i = 0 ; i < N ; i++) {
        for (j = 0; j < N; j++) {
            printf("%d%s", board[i][j], board[i][j] >= 10 ? " " : "  ");
        }
        printf("\n");
    }

    double time_solution = (((double) t) / CLOCKS_PER_SEC);
    
    printf("\nThe solution took %f seconds to be found", time_solution);
}

