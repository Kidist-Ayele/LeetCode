class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        #Step1: before sorting map the index with the value
        query_map = {}
        for index,query in enumerate(queries):
            query_map[index] = query
        
        #Step2: sort both the queries and the items
        queries.sort()
        items.sort()
        max_beauties = {}
        max_beauty = 0
        index = 0

        #Step3: use two pointers approach the for while combo and update the max beauty accordingly
        for query in queries:
            while index < len(items) and query >= items[index][0]:
                max_beauty = max(max_beauty,items[index][1])
                index += 1
            max_beauties[query] = max_beauty
        
        #Step4: build our answer based on the max beauty for each query
        answer = []
        for index, val in query_map.items():
            res = max_beauties[val]
            answer.append(res)

        return answer
        