class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        index = 0
        while index < len(path):
            if path[index] == '/':
                index += 1
                continue
            file_name = []
            while index < len(path) and path[index] != '/':
                file_name.append(path[index])
                index += 1
            file_name = ''.join(file_name)
            if file_name == '.':
                continue
            elif file_name == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(file_name)
        if not stack:
            return '/'
        return '/' + '/'.join(stack)