class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.lower()
        arr = []

        if len(s) == 0:
            return True
        for char in s:
            char = char.lower()
            if char.isalpha() or char.isdigit():
                arr.append(char)
       
        right = len(arr) - 1
        left = 0

        while left <= right:
            if arr[left] != arr[right]:
                return False
            
            right -= 1
            left += 1
    
        return True
        