class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        l = len(p)
        ans  = []
        left = 0
        counter_p = Counter(p)
        my_dict = defaultdict(int)
        for right in range(n):
            if s[right] in counter_p:
                my_dict[s[right]] += 1

                if right - left + 1 > l:
                    my_dict[s[left]] -= 1
                    if my_dict[s[left]] == 0:
                        del my_dict[s[left]]  # Clean up 0 counts
                    left += 1  
            else:
                my_dict.clear()
                left = right + 1
            if my_dict == counter_p:
                ans.append(left)
        return ans


        

        