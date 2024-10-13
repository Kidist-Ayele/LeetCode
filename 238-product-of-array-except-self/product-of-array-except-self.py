class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        product = 1
        zero_count = nums.count(0)
         # Calculate the product of all non-zero numbers
        for num in nums:
            if num != 0:
                product *= num
        for i in range(len(nums)):
            if zero_count == 0:
                ans.append((product // nums[i]))
            elif zero_count == 1:
                if nums[i] == 0:
                    ans.append(product)
                else:
                    ans.append(0)
            else:
                ans.append(0)
        return ans

        