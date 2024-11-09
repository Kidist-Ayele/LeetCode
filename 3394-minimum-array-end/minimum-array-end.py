class Solution:
    def minEnd(self, n: int, x: int) -> int:
        shifts = [i for i in range(64) if not (x & (1 << i))]
        cur = x
        calc = n - 1
        i = 0

        while calc > 0:
            cur |= (calc & 1) << shifts[i]
            calc >>= 1
            i += 1

        return cur
