class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_stack(string):
            stack = []
            for char in string:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return stack
        stack_s = build_stack(s)
        stack_t = build_stack(t)
        return stack_s == stack_t

        