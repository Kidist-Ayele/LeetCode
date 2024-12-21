class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = nums.count(1)
        n = len(nums)
        extended_nums = nums + nums
        left, right = 0, 0
        cnt = 0
        ans = n + 1
        while right < n * 2:
            if extended_nums[right] == 0:
                cnt += 1
            while right - left + 1 > k:
                if extended_nums[left] == 0:
                    cnt -= 1
                left += 1
            if right - left + 1 == k:
                ans = min(ans, cnt)
            right += 1
        return ans
            

