class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        res = 0
        odd_count = 0
        prefix = 0
        for right in range(len(nums)):
            if nums[right] % 2 != 0:
                odd_count += 1
                prefix = 0
            while odd_count == k:
                if nums[left] % 2 != 0:
                    odd_count -= 1
                prefix += 1 
                left += 1
            res += prefix 
            
                
        return res
                

                