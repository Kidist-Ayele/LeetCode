class Solution:
    def minChanges(self, s: str) -> int:
        cnt = right = 0
        while right < len(s) - 1:
            if s[right] != s[right + 1]:
                cnt += 1
            right += 2
        return cnt
            
        