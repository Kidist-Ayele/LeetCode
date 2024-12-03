class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        def check(k):
            left = right = cnt = 0
            for right in range(len(nums)):
                if nums[right] % 2 != 0:
                    k -= 1
                while k < 0:
                    if nums[left] % 2 != 0:
                        k += 1
                    left += 1
                    
                cnt += (right - left + 1)
            return cnt
        return check(k) - check(k - 1)
            