class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        copy_nums1 = nums1[:m]
        total = 0

        while i<m and j<n:
            
            if copy_nums1[i] < nums2[j]:
                nums1[total] = copy_nums1[i]
                total += 1
                i = i + 1

            else:
                nums1[total] = nums2[j]
                total += 1
                j = j + 1

        while j < n:
            nums1[total] = nums2[j]
            j = j + 1
            total += 1

        while i < m:
            nums1[total] = copy_nums1[i]
            i = i + 1
            total += 1
