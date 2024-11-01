class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = s[0]
        cnt = 1
        for right in range(1,len(s)):
            if s[right] == ans[-1]:
                cnt += 1
                if cnt < 3:
                    ans += s[right]
            else:
                cnt = 1
                ans += s[right]
        return ans
            
            



        