class Solution(object):
    def rotate(self, nums, k):
        arr = [0] * len(nums)
        k = k % len(nums)
        for i in range(len(nums)):
            New_Index = (i + k) % len(nums)
            arr[New_Index] = nums[i]
        nums[:] = arr
        # return nums
        