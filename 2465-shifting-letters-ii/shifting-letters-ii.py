class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
      
        direct = [0] * (len(s) + 1)
        
        for start, end, direction in shifts:
            if direction == 1:
                direct[start] += 1 
                if end + 1 < len(s):
                    direct[end + 1] -= 1
            else:
                direct[start] -= 1
                if end + 1 < len(s):
                    direct[end + 1] += 1

        running_sum = 0
        prefix_sum = [0] * len(s)
        result = []
        for i in range(len(s)):
            running_sum += direct[i]
            prefix_sum[i] = running_sum
            
        
        for i in range(len(s)):
            shift_value = (ord(s[i]) - ord('a') + prefix_sum[i]) % 26
            shift_value = (shift_value + 26) % 26
            result.append(chr(ord('a') + shift_value))
            
        return ''.join(result)


