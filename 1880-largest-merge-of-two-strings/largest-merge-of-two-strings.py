class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        left = right = 0
        merg = ""
        while left < len(word1) and right < len(word2):
            if word1[left:] > word2[right:]:
                merg += word1[left]
                left += 1
            else:
                merg += word2[right]
                right += 1
        if left < len(word1):
            merg += word1[left:]
        if right < len(word2):
            merg += word2[right:]
        return merg


        