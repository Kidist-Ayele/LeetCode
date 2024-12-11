class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        k = []
        for i in range(n):
            cur_max = max(arr[:n - i])
            max_inx = arr.index(cur_max) + 1
            arr[:max_inx] = reversed(arr[:max_inx])

            k.append(max_inx)

            arr[:n - i] = reversed(arr[:n - i])
            
            k.append(n - i)
        return k
        