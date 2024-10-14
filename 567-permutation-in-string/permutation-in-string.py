class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k, n = len(s1), len(s2)

        if k > n:
            return False

        my_dict = defaultdict(int)
        s1_count = Counter(s1)
        left = 0

        for right in range(n):
            my_dict[s2[right]] += 1

            if right - left + 1 > k:
                my_dict[s2[left]] -= 1
                if my_dict[s2[left]] == 0:
                    del my_dict[s2[left]]  
                left += 1  
            if my_dict == s1_count:
                return True
        return False


        