class Solution(object):
    def hIndex(self, citations):   
        n = len(citations)
        bucket = [0] * (n + 1)
        for c in citations:
            if c >= n:
                bucket[n] += 1
            else:
                bucket[c] += 1
        h = n
        papers = 0
        while h >= 0:
            papers += bucket[h]
            if papers >= h:
                return h
            h -= 1
        return 0


# class Solution(object):
#     def hIndex(self, citations):
#         citations.sort()
#         for i in range(0, len(citations)):
#             h = len(citations) - i
#             if citations[i] >= h:
#                 return h
#         return 0