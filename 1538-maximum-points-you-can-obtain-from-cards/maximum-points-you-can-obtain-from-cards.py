class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints[len(cardPoints) - k:])
        # print(total)
        cur_max = total
        left, right = 0, len(cardPoints) - k
        while right < len(cardPoints) and left < k:
           
            total += cardPoints[left] - cardPoints[right]
            cur_max = max(cur_max, total)
            left += 1
            right += 1
        return cur_max
