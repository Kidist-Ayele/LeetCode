class Solution:
    def maxArea(self, height: List[int]) -> int:
        left , right = 0, len(height) - 1
        cur_min = 1
        res = 0
        while left < right:
            cur_min = min(height[left], height[right])
            ans = cur_min * (right - left)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            res = max(res, ans)
        return res
        