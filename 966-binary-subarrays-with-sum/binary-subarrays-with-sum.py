class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(x):
            # If x is negative, no valid subarray can have a sum less than 0
            if x < 0:
                return 0
            res = left = cur = 0
            for right in range(len(nums)):
                cur += nums[right]
                # Shrink the window while the current sum is greater than x
                while cur > x :
                    cur -= nums[left]
                    left += 1
                # Count the number of subarrays from left to right
                res += (right - left + 1)
            return res

        return helper(goal) - helper(goal - 1)