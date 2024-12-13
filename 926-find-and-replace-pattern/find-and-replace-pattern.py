class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            if len(word) != len(pattern):
                continue
            else:
                my_dict = {}
                reverse_dict = {}
                flag = True
                for i, char in enumerate(pattern):
                    if char in my_dict:
                        if my_dict[char] != word[i]:
                            flag = False
                            break
                    elif word[i] in reverse_dict:
                        if reverse_dict[word[i]] != char:
                            flag = False
                            break
                    else:
                        reverse_dict[word[i]] = char
                        my_dict[char] = word[i]
                if flag:
                    ans.append(word)
        return ans
        