class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) <= 1:
            return [strs]
        seen = {}
        
        for string in range(len(strs)):
            key = "".join(sorted(strs[string]))
            if key not in seen:
                seen[key] = [strs[string]]
            else:
                seen[key].append(strs[string])
        strs = list(seen.values())
        return strs