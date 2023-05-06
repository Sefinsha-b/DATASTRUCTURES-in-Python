# Leetcode 561 array partition.
from ast import List
from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int])->int:
        nums.sort()
        sum_min=0
        for i in range(len(nums),2):
            sum_min +=nums[i]
            return sum_min
s = Solution()
nums = [1,4,3,2]
output = s.arrayPairSum(nums)
print(output)
# # Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

 

# Example 1:

# Input: nums = [1,4,3,2]
# Output: 4
# # Explanation: All possible pairings (ignoring the ordering of elements) are:
# # 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
# # 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
# # 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
# # So the maximum possible sum is 4.
