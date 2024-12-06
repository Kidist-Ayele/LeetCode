class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        all_distance = []
        for row in range(len(points)):
            x, y = points[row][0], points[row][1]
            point_dis = x ** 2 + y ** 2
            all_distance.append([point_dis, points[row]])
        
        all_distance.sort()
        result = []
        for i in range(k):
            result.append(all_distance[i][1])
        return result

