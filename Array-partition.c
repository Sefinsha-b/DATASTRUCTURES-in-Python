#include <stdio.h>
#include <stdlib.h>

int cmpfunc(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int arrayPairSum(int* nums, int numsSize) {
    int sum_min = 0;
    qsort(nums, numsSize, sizeof(int), cmpfunc);
    for (int i = 0; i < numsSize; i += 2) {
        sum_min += nums[i];
    }
    return sum_min;
}

int main() {
    int nums[] = {1, 4, 3, 2};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int output = arrayPairSum(nums, numsSize);
    printf("%d\n", output);
    return 0;
}
