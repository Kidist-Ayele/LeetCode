class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        ans = []
        n = len(nums)
        product = 1
        for i in range(n):
            if nums[i] != 0:
                product *= nums[i]

        if counter[0] > 1:
            ans = [0] * n
        elif counter[0] == 1:
            for num in nums:
                if num == 0:
                    ans.append(product)
                else:
                    ans.append(0)
        else:
            for num in nums:
                ans.append(product // num)
        return ans 
                




        