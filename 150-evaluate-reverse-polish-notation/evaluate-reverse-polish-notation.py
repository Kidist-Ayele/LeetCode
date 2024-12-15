class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operate(token,a,b):
            if token == '+':
                return a + b
            elif token == '-':
                return a - b
            elif token == '*':
                return a * b
            else:
                return int(a/b)
        operators = ['+','-','*','/']
        stack = []
        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                ans = operate(token,a,b)
                stack.append(ans)
            else:
                stack.append(int(token))
        return stack[0]