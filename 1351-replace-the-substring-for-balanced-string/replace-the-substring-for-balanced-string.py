from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        # Helper function to check if the current window satisfies the condition

        def isValid():
            for char in changed:
                if window[char] < changed[char]:  
                    return False
            return True
        counter = Counter(s)  # Count the occurrences of each character in the string
        n = len(s)
        limit = n // 4  # Each character (Q, W, E, R) should not exceed n/4 times
        changed = {}
        window = Counter()  # To track the characters in the current sliding window
        ans = n
            
        # Prepare the 'changed' dictionary for characters that need to be reduced in count
        for char in counter:
            if counter[char] > limit:
                changed[char] = counter[char] - limit 

        if not changed: 
            return 0

        left = 0
        # Sliding window approach
        for right in range(n):
            if s[right] in changed:
                window[s[right]] += 1
            
            while isValid():
                ans = min(ans, right - left + 1)  
                if s[left] in window:
                    window[s[left]] -= 1  
                left += 1

        return ans  
