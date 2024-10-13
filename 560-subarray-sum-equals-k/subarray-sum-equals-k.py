class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        my_dict = {}
        counter = 0
        for i in range(len(nums)):
            total += nums[i]
            if total == k:
                counter += 1
            if (total - k) in my_dict:
                counter += my_dict[total - k]
            if total in my_dict:
                my_dict[total] += 1
            else:
                my_dict[total] = 1
        return counter


        