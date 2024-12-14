class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        cur_max = 0
        left = right = 0 
        for right in range(k):
            if s[right] in vowels:
                cur_max += 1
        max_val = cur_max
        right = k
        while right < len(s):
            if s[right] in vowels:
                max_val += 1
            if right - left + 1 > k:
                if s[left] in vowels:
                    max_val -= 1
                left += 1
            cur_max = max(cur_max, max_val)
            right += 1
        return cur_max
            
        