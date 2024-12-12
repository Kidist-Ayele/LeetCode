class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        cur_count = blocks[:k].count('W')
        left = 0
        res = cur_count
        for right in range(k, len(blocks)):
            if blocks[right] == 'W':
                cur_count += 1
            if blocks[left] == 'W':
                cur_count -= 1
            left += 1
            res = min(res, cur_count)
        return res