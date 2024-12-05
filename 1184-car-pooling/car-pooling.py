class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cur_max = 0
        rows= len(trips)

        for row in range(rows):
            cur_max = max(cur_max, max(trips[row][1:]))
        cur_passengers = [0] * (cur_max + 1)
        # print(cur_max)
        for row in range(rows):
            val, start, end = trips[row][0], trips[row][1], trips[row][2]
            cur_passengers[start] += val
            if end < len(cur_passengers):
                cur_passengers[end] -= val
        prefix_sum = 0
        for num in cur_passengers:
            prefix_sum += num
            if prefix_sum > capacity:
                return False
        return True


        