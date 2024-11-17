class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = x
        y = 0
        
        if x < 0:
            return False
        else: 
            while nums > 0:
                y = (y * 10) + nums % 10
                nums //= 10
            return x == y