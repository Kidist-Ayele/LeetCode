class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        new_s = ""
        
        for char in s:
            char = char.lower()
            if char in letters or char.isdigit():
                new_s += char
        left, right = 0, len(new_s) - 1
        while left <= right:
            if new_s[left] != new_s[right]:
                return False
            left += 1
            right -= 1
        return True

        

        
        