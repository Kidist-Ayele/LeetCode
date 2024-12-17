class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = 0
        for num in nums:
            total += num

        need = total - x
        if need < 0:
            return -1
        
        if need == 0:
            return len(nums)
        check = 0
        max_len = 0
        left , right = 0, 0
        while right < len(nums):
            check += nums[right]

            while check > need and left < right:
                check -= nums[left]
                left += 1
            if check == need:
                max_len = max(max_len, right - left + 1)
            right += 1
        return len(nums) - max_len if max_len != 0 else -1


        