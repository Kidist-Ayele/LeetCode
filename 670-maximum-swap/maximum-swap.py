class Solution:
    def maximumSwap(self, num: int) -> int:
        cur = str(num)
        cur = list(cur)
        answer = num
        maxi = max(cur)
        for i in range(len(cur)):
            for j in range(i+1,len(cur)):
                cur[i], cur[j] = cur[j], cur[i]
                current = int(''.join(cur))
                answer = max(answer,current)
                cur[i], cur[j] = cur[j], cur[i]
        return answer