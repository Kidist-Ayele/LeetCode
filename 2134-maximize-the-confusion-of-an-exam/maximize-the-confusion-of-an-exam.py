class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def max_with_char(cur_char, k):
            left = 0
            ans = 0
            for right in range(len(answerKey)):
                if answerKey[right] != cur_char:
                    k -= 1
                while k < 0:
                    if answerKey[left] != cur_char:
                        k += 1
                    left += 1
                
                ans = max(ans, right - left + 1)
            return ans
        return max(max_with_char('T', k), max_with_char('F', k))



        