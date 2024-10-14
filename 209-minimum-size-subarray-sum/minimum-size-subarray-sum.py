class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        n = len(nums)
        num_sum = 0
        res = n + 1
        for right in range(n):
            num_sum += nums[right]
            while num_sum >= target:
                res = min(res, right - left + 1)
                num_sum -= nums[left]
                left += 1
                
        return res if res <= n else 0







        # sub_len = float('inf')
        # while right < n: 
        #     num_sum += nums[right]  
            
        #     while num_sum >= target:  
        #         sub_len = min(sub_len, right - left + 1)  
        #         num_sum -= nums[left]  
        #         left += 1  
            
        #     right += 1  
        # return sub_len if sub_len != float('inf') else 0
        