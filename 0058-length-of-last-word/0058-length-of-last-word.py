class Solution(object):
    def lengthOfLastWord(self, s):
        right = len(s) - 1
        count = 0
        while s[right] == ' ':
            right -= 1
        while right >= 0 and s[right] != ' ':
            count += 1
            right -= 1
        return count