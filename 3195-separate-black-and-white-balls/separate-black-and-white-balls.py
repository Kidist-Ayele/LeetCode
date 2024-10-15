class Solution:
    def minimumSteps(self, s: str) -> int:
        stop = right = len(s) - 1
        ans = 0
        while right >= 0 and s[right] == '1':
            stop = right
            right -= 1  
        for i in range(stop, -1, -1):
            if s[i] == '0':
                continue
            ans += stop - i
            stop -= 1
           
        return ans
                
