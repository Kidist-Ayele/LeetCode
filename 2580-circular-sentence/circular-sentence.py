class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        n = len(sentence)
        new_s = sentence.split()
        if sentence[0] != sentence[n - 1]:
            return False
            
        for r in range(len(new_s) - 1):
            if new_s[r][-1] != new_s[r + 1][0]:
                return False
        return True


        