class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        bucket = []
        for i in range(len(nums) + 1):
            bucket.append([])

        for num, count in freq.items():
            bucket[count].append(num)

        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result



# class Solution(object):
#     def topKFrequent(self, nums, k):

#         freq = {}
#         for i in range(len(nums)):
#             freq[nums[i]] = freq.get(nums[i], 0) + 1

#         sorted_items = sorted(freq.items(), key=lambda item: item[1], reverse=True)

#         result = []
#         for num, count in sorted_items[:k]:
#             result.append(num)

#         return result
