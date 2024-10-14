class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans= window = sum(nums[:k])

        left, right = 0, k
        while right < len(nums):
            window += nums[right]
            window -= nums[left]
            ans = max(ans, window)
            right += 1
            left += 1
        return ans / k

        
