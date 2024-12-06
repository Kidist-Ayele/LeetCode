class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remender_count = defaultdict(int)
        prefix_sum = 0
        remender = ans = 0
        remender_count[0] = 1

        for i in range(len(nums)):
            prefix_sum += nums[i]
            remender = prefix_sum % k
            if remender < 0:
                remender += k
            
            ans += remender_count[remender]
            remender_count[remender] += 1
        return ans

        
        