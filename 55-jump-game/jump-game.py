class Solution:
    def canJump(self, nums: List[int]) -> bool:
        check = 0
        for num in nums:
            if check < 0:
                return False
            elif num > check:
                check = num
            check -= 1
        return True

        