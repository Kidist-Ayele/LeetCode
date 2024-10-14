class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        cnt_w = blocks[:k].count('W')
        res = cnt_w

        for right in range(k, len(blocks)):
            if blocks[right] == 'W':
                cnt_w += 1
            if blocks[left] == 'W':
                cnt_w -= 1
            left += 1
            res = min(res, cnt_w)
        return res

            

        