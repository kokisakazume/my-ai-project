from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,num in enumerate(nums):
            result = target - num
            if result in seen:
                return (seen[result],i)
            seen[num] = i


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))