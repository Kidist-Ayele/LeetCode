class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        uniq_set = set()
        total = 0
        n = len(nums)
        left = right = 0
        cur_max = 0
        while right < n:
            # Expand the window with right pointer until we find duplicate
            if nums[right] not in uniq_set:
                uniq_set.add(nums[right])
                total += nums[right]
                right += 1
            else:
                # Shrink the window by moving the left pointer until the duplicate is removed
                uniq_set.remove(nums[left])
                total -= nums[left]
                left += 1
            cur_max = max(cur_max, total)
        return cur_max

        