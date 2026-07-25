class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        strs.sort(key=len)
        prefix = strs[0]
        for word in strs:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

        