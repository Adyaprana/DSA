class Solution(object):
    def rotate(self, nums, k):
        # nums[:] = nums[::-1]
        k = k % len(nums)
        nums.reverse()
        nums[0:k] = nums[0:k][::-1]
        nums[k:] = nums[k:][::-1]
      

# class Solution(object):
#     def rotate(self, nums, k):
#         arr = [0] * len(nums)
#         k = k % len(nums)
#         for i in range(len(nums)):
#             New_Index = (i + k) % len(nums)
#             arr[New_Index] = nums[i]
#         nums[:] = arr
        