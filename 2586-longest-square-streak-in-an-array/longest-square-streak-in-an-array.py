class Solution:
    def longestSquareStreak(self, nums):

        #       #       #        #
        #  THIS IS COPIED BY MS  #
        #       #       #        #

        mp = {}
        nums.sort()
        res = -1

        for num in nums:
            sqrt = isqrt(num)

            if sqrt * sqrt == num and sqrt in mp:
                mp[num] = mp[sqrt] + 1
                res = max(res, mp[num])
            else:
                mp[num] = 1

        return res