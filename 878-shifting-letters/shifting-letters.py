class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prefix_sum = list(accumulate(reversed(shifts)))
        prefix_sum = list(reversed(prefix_sum))
        ans = ""
        for i in range(len(s)):
            ans += chr((ord(s[i]) - ord("a") + prefix_sum[i]) % 26 + ord("a")) 
        return ans

        