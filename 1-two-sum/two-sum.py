from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted((num, i) for i, num in enumerate(nums))
        left, right = 0, len(nums_sorted) - 1
        
        while left < right:
            total = nums_sorted[left][0] + nums_sorted[right][0]
            if total == target:
                return [nums_sorted[left][1], nums_sorted[right][1]]
            elif total > target:
                right -= 1
            else:
                left += 1