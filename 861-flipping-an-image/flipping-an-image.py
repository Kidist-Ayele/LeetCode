class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for row in range(len(image)):
            left, right = 0, len(image[row]) - 1
            while left <= right:
                if image[row][left] == 1 and image[row][right] == 1:
                    image[row][left] = 0
                    image[row][right] = 0
                elif image[row][left] == 0 and image[row][right] == 0:
                    image[row][left] = 1
                    image[row][right] = 1
                left += 1
                right -= 1
        return image
                    
        