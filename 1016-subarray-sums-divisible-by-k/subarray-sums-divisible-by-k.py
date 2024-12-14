class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        running_sum = 0
        remender_cnt = defaultdict(int)
        remender_cnt[0] = 1
        ans = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            remainder = running_sum % k
            
            ans += remender_cnt[remainder]
            remender_cnt[remainder] += 1
        return ans



        