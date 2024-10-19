class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0: -1}  
        current_sum = 0
        
        for i in range(len(nums)):
            current_sum += nums[i]  
            if k != 0:
                current_sum %= k
            
            if current_sum in remainder_map:
                if i - remainder_map[current_sum] > 1:
                    return True
            else:
                remainder_map[current_sum] = i
        
        return False

        