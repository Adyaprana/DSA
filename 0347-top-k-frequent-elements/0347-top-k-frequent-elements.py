class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        # sorted_desc = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        # result = list(sorted_desc.keys())[:k]
        
        sorted_items = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        result = []
        for num, count in sorted_items[:k]:
            result.append(num)
        return result
