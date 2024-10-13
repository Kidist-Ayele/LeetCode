class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # Each element is a descent period by itself
        total = len(prices)
        left, right = 0, 1
        # Check descent
        while right < len(prices):
            if prices[right - 1] - prices[right] == 1:
                #  Increment total by the number of descent periods formed
                total += (right - left)
            else:
                # reset left to the current right
                left = right
            right += 1
            
        return total


        