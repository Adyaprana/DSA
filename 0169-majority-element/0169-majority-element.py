class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        votes = 0
        for num in nums:
            if votes == 0:
                candidate = num
                votes += 1
            elif num == candidate:
                votes +=1
            else:
                votes -= 1
        return candidate    