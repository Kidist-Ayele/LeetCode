class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        left, right = 0, 0
        cur_vowels = res = 0

        for right in range(len(s)):
            if s[right] in vowels:
                cur_vowels += 1
            while (right - left + 1) > k:
                if s[left] in vowels:
                    cur_vowels -= 1
                left += 1
            res = max(res, cur_vowels)
        return res

