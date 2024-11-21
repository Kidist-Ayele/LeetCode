class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  
            return ""
        
        strs.sort()
        first, last = strs[0], strs[-1]
        ans = ""
        n = min(len(first), len(last))
        for i in range(n):
            if first[i] == last[i]:
                ans += first[i]
            else:
                break
        return ans
