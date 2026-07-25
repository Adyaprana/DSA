class Solution(object):
    def findDisappearedNumbers(self, nums):
        st = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        # return nums
        for i in range(len(nums)):
            if nums[i] > 0:
                st.append(i +1)
        return st
                