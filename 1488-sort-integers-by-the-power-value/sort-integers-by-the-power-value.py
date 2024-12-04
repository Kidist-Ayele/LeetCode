class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        my_dict = defaultdict(int)
     
        for num in range(lo, hi + 1):
            steps  = 0
            cur_val = num
            while cur_val != 1:
                if cur_val % 2 == 0:
                    cur_val //=  2
                else:
                    cur_val = 3 * cur_val + 1
                steps += 1
            my_dict[num] = steps
        sorted_list = []

        for key, val in my_dict.items():
            sorted_list.append([val,key])
            
        sorted_list.sort()
        return sorted_list[k-1][1]
        
            
        