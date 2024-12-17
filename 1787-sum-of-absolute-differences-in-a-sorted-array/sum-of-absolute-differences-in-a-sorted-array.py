class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        n = len(nums)
        left = right = 0
        result = []
        for i in range(n):
            left = i * nums[i] - prefix[i]
            right = (prefix[n] - prefix[i + 1]) - nums[i] * (n - i - 1)
            result.append(left + right)
        return result

        