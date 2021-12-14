# @before-stub-for-debug-begin
from python3problem1 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ss = dict()
        for i, x in enumerate(nums):
            if x in ss:
                return [ss[x], i]
            ss[target - x] = i
# @lc code=end

