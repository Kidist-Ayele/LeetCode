class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for left in range(len(nums) - 1):
            for right in range(left + 1, len(nums)):
                if str(nums[left]) + str(nums[right]) < str(nums[right]) + str(nums[left]):
                    nums[left], nums[right] = nums[right], nums[left]
        larg_num = ''.join(map(str,nums))
        return str(int(larg_num))


        