class Solution(object):
    def productExceptSelf(self, nums):
        answer = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                left_product = 1
            else:
                left_product *= nums[i-1]  
            answer[i] = (left_product)

        for i in reversed(range(len(nums))):
            if i == len(nums)-1:
                right_product = 1
            else:
                right_product *= nums[i+1]
            answer[i] *= right_product
        return answer   
