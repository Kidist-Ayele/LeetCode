class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = right = 0 
        n = len(answerKey)
        res = 0  
        max_t = max_f = 0  
        my_dict = {char:0 for char in "TF"}

        for right in range(len(answerKey)):
            my_dict[answerKey[right]] += 1
            
            while min(my_dict['T'], my_dict['F']) > k:
                my_dict[answerKey[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
       