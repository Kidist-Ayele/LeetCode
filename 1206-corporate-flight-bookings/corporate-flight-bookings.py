class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        max_len = 0
        rows = len(bookings)
       
        cur_range = [0] * (n + 1)
        for row in range(rows):
            first, last, val = bookings[row][0], bookings[row][1], bookings[row][2]
            cur_range[first] += val
            if last + 1 < len(cur_range):
                cur_range[last + 1] -= val

        prefix_sum = 0
        result = []
        for i in range(1, len(cur_range)):
            if result:
                result.append(result[-1] + cur_range[i])
            else:
                result.append(cur_range[i])
         
        return result


        