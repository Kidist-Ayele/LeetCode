class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_dict = defaultdict(int)
        left = right = maxlen = 0
        while right < len(s):
            my_dict[s[right]] += 1
            
            while (right - left + 1) - max(my_dict.values()) > k:
                my_dict[s[left]] -= 1
                left += 1

            maxlen = max(maxlen, right - left + 1)
            right += 1
        return maxlen
               
        