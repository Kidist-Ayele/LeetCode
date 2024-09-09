class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left, right = 0, len(cardPoints) - k
        # Calculate the sum of the last 'k' elements
        total = sum(cardPoints[right:])
        result = total
        # Slide the window to the left one element at a time
        while right < len(cardPoints):
            # Update the total by adding the leftmost element and subtracting the rightmost element
            total += (cardPoints[left] - cardPoints[right])
            result = max(result, total)
            right += 1
            left += 1
        return result

        
        