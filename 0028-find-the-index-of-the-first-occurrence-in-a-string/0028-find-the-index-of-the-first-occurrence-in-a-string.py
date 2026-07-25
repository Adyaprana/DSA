class Solution(object):
    def strStr(self, haystack, needle):
        if needle not in haystack:
            return -1

        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        