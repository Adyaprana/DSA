class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p1 = m - 1
        p2 = n - 1
        write = m + n - 1
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[write] = nums1[p1]
                p1 -= 1
            else:
                nums1[write] = nums2[p2]
                p2 -= 1
            write -= 1
        return nums1

# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         k = 0
#         for i in range(len(nums1)):
#             if i >= m:
#                 nums1[i] = nums2[k]
#                 k += 1
#         nums1.sort()
#         return nums1