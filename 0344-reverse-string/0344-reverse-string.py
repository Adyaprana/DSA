class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = 0
        k = len(s) // 2
        for i in range(len(s)-1 , k-1, -1):
                s[i] , s[n] = s[n], s[i]
                n += 1
        return s 


