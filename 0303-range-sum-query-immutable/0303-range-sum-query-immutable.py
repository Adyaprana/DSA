class NumArray(object):

    def __init__(self, nums):
        self.prefix = []
        running_sum = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            self.prefix.append(running_sum)

    def sumRange(self, left, right):
            if left == 0:
                return self.prefix[right]
            else:
                return self.prefix[right] - self.prefix[left-1]



        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)