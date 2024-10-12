from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total = right = left = cnt = 0
        prefix_sum = {0: 1}
        
        while right < len(nums):
            total += nums[right] 
            # Check if there exists a subarray with the required sum
            if total - goal in prefix_sum:
                cnt += prefix_sum[total - goal]  # Increment count by the number of times (total - goal) has been seen
            
            # Update the frequency of the current prefix sum in the dictionary
            if total in prefix_sum:
                prefix_sum[total] += 1
            else:
                prefix_sum[total] = 1

            right += 1  # Move the right pointer forward to expand the window
        
        return cnt  # Return the number of subarrays with the sum equal to the goal
