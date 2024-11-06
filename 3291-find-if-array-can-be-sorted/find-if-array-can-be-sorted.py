from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prev_max = 0  
        curr_min = curr_max = nums[0]  
        prev_count = nums[0].bit_count()  
        for num in nums:
            curr_count = num.bit_count()  
            
            if prev_count == curr_count:
                curr_min = min(curr_min, num)
                curr_max = max(curr_max, num)
            
            elif curr_min < prev_max:
                return False  
            else:
                prev_max = curr_max  
                curr_min = curr_max = num  
                prev_count = curr_count  

        return curr_min >= prev_max
