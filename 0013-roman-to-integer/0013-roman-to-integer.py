class Solution(object):
    def romanToInt(self, s):
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
        ans = 0        
        for i in range(0, len(s)):
            if i < len(s)-1:
                if roman[s[i]] < roman[s[i+1]]:
                    ans -= roman[s[i]]
                elif roman[s[i]] >= roman[s[i+1]]:
                    ans += roman[s[i]]
            elif i == len(s)-1:
                ans += roman[s[i]]
        return ans