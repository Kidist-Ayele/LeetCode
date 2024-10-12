class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = right = 0
        total_cnt = 3
        cur_cnt = 0
        hash_map = {key:0 for key in "abc"}
        result = 0
        while right < len(s):
            cur_char = s[right]
            # Increase the count for the current character in the window
            if hash_map[cur_char] == 0:
                cur_cnt += 1
            hash_map[cur_char] += 1
            # Shrink the window from the left if all 'a', 'b', and 'c' are in the current window
            while cur_cnt == total_cnt and left <= right:
                result += len(s) - right
                hash_map[s[left]] -= 1
                # Remove the leftmost character from the window
                if hash_map[s[left]] == 0:
                    cur_cnt -= 1

                left += 1
            right += 1
        return result

        