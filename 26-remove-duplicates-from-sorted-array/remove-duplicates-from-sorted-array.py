class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        check = set()
        k = 0
        for i in range(len(nums)):
            if nums[i] not in check:
                nums[k] = nums[i]
                check.add(nums[i])
                k += 1
                
        return k
        