class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        cnt = 0
        while left < right:
            cur_sum = people[left] + people[right]
            if cur_sum <= limit:
                cnt += 1
                right -= 1
                left += 1
            else:
                right -= 1
        if cnt * 2 != len(people):
            cnt += len(people) - (cnt * 2)
        return cnt

        

        