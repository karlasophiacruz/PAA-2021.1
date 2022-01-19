#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int min(int days[], int arr[]) {
    return days[arr[0]] <= days[arr[1]] ? arr[0] : arr[1];
}

int max(int days[], int arr[]) {
    return days[arr[0]] >= days[arr[1]] ? arr[0] : arr[1];
}

int* max_profit(int days[], int bs_left[], int bs_right[], int bs_total[]) {
    int left = days[bs_left[1]] - days[bs_left[0]];
    int right = days[bs_right[1]] - days[bs_right[0]];
    int total = days[bs_total[1]] - days[bs_total[0]];
    
    if (left >= right) {
        if (left >= total) {
            return bs_left;
        }
        return bs_total;
    }

    return right >= total ? bs_right : bs_total;
}

int *trade(int days[], int i, int n) {
 int m = (i + n) / 2;
 
    if ((i == n - 1) || i == n) {
        int* temp = malloc(2 * sizeof (int));

        temp[0] = i;
        temp[1] = n;
        
        return temp;
    }  

    int* buy_sell_left = trade(days, i, m);
    int* buy_sell_right = trade(days, m + 1, n);

    int* buy_sell_total = malloc(2 * sizeof (int));

    buy_sell_total[0] = min(days, buy_sell_left);
    buy_sell_total[1] = max(days, buy_sell_right);    
    
    return max_profit(days, buy_sell_left, buy_sell_right, buy_sell_total);
}