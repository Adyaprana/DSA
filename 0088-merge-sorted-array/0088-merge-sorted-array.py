class Solution(object):
    def merge(self, nums1, m, nums2, n):
        k = 0
        for i in range(len(nums1)):
            if i >= m:
                nums1[i] = nums2[k]
                k += 1
        nums1.sort()
        return nums1
