class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for left in range(len(nums) - 1):
            for right in range(left + 1, len(nums)):
                if nums[left] > nums[right]:
                    nums[left], nums[right] = nums[right], nums[left]

        