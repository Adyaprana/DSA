class Solution(object):
    def hIndex(self, citations):
        # if len(citations) == 1:
        #     return int(citations[0])
        citations.sort()
        for i in range(0, len(citations)):
            h = len(citations) - i
            if citations[i] >= h:
                return h
        # return citations[0]
        return 0