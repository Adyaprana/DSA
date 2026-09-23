class Solution(object):
    def isIsomorphic(self, s, t):
        check = {} 
        for i in range(len(s)):
            if s[i] in check:
                if check[s[i]] == t[i]:
                    continue
                else:
                    return False

            elif t[i] in check.values():
                return False
                
            else:
                check[s[i]] = t[i]
        return True