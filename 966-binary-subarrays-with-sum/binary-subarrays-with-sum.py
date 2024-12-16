class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        my_dict = defaultdict(int)
        my_dict[0] = 1
        running_sum = 0
        res = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            if running_sum - goal in my_dict:
                res += my_dict[running_sum - goal] 
            my_dict[running_sum] += 1
        return res

        