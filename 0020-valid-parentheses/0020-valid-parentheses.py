class Solution(object):
    def isValid(self, s):
        stack = []
        d = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for i in s:
            if i in d.values():
                stack.append(i)
            if i in d.keys():
                if len(stack) == 0:
                    return False
                if d[i] != stack[-1]:
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        return False