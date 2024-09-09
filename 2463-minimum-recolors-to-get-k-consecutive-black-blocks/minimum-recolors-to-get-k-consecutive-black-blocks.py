class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        # Count the number of 'W's on the first window
        first_window = Counter(blocks[:k])
        cur_min = first_window['W']
        cnt_W = first_window['W']
        n= len(blocks)
        # Iterate through blocks with a sliding window of size k
        while left < n - k:
            # Check if the new character entering the window is 'W'
            if blocks[left + k] == 'W':
                cnt_W += 1
            # Check if the character leaving the window is 'W'
            if blocks[left] == 'W':
                cnt_W -= 1
            cur_min = min(cur_min, cnt_W)
            left += 1
        return cur_min
            
            

        