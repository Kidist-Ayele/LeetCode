class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        right = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[right]:
                stack.pop()
                right += 1
        
        return not stack
        