class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        cur_max = 0
        left = right = 0 
        max_val = 0
        while right < len(s):
            if s[right] in vowels:
                max_val += 1
            while right - left + 1 > k:
                if s[left] in vowels:
                    max_val -= 1
                left += 1
            cur_max = max(cur_max, max_val)
            right += 1
        return cur_max
            
        