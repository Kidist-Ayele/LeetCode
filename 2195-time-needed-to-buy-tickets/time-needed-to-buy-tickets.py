class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        for i in range(len(tickets)):
            queue.append([i, tickets[i]])
        ans = 0
        while queue :
            ans += 1
            index, cur = queue.popleft()
            if cur - 1 > 0:
                queue.append([index,cur - 1])
            elif index == k:
                return ans 
        return ans 

        