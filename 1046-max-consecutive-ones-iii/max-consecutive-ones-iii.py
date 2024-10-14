class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        left = right =0
        cnt_zero = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                cnt_zero += 1
            while cnt_zero > k:
                if nums[left] == 0:
                    cnt_zero -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
