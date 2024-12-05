class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1]
        for num in nums[:-1]:
            left_product.append(left_product[-1] * num)
        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            left_product[i] *= right_product
            right_product *= nums[i]
        return left_product





        