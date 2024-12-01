class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        counter = 0
        ans = 0
        for char in s:
            if char == c:
                counter += 1
                ans += counter
        return ans



        