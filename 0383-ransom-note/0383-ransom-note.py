class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        seen = {}
        for i in magazine:            
            # if i not in seen:
            #     seen[i] = seen.get(i, 0) + 1
            # elif i in seen:
            #     seen[i] += 1
            seen[i] = seen.get(i, 0) + 1
            
        for i in ransomNote:
            if i not in seen or seen[i] == 0:
                return False
            seen[i] -= 1
        return True