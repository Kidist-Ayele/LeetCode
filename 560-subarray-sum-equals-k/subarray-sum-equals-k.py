class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_cnt = defaultdict(int)
        prefix_sum_cnt[0] = 1
        prefix_sum = 0
        ans = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum - k in prefix_sum_cnt:
                ans += prefix_sum_cnt[prefix_sum - k]
           
            prefix_sum_cnt[prefix_sum] += 1
        return ans

        