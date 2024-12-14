class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_len = 0
        for row in trips:
            val, left, right = row
            max_len = max(max_len, left, right)
        direction = [0] * (max_len + 1)
        for row in trips:
            val, left, right = row
            direction[left] += val
            if right < len(direction):
                direction[right] -= val
        running_sum = 0
        for i in range(len(direction)):
            running_sum += direction[i]
            if running_sum > capacity:
                return False
        return True


        