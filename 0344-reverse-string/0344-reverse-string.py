class Solution(object):
    def reverseString(self, s):
        # two pointer 
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        # single pointer
        # n = 0
        # for i in range(len(s)-1 , (len(s) // 2) -1, -1):
        #         s[i] , s[n] = s[n], s[i]
        #         n += 1