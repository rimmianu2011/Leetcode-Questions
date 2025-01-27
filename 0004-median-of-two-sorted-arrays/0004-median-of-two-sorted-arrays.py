class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            a = nums1
            b = nums2
        else:
            a = nums2
            b = nums1
        total = len(nums1) + len(nums2)
        half = total // 2

        l, r = 0, len(a) - 1
        

        while True:
            m = (l + r) // 2
            rem = half - m - 2
            aLeft = a[m] if m>=0 else float ('-infinity')
            aRight = a[m+1] if (m+1)<len(a) else float ('infinity')
            bLeft = b[rem] if rem>=0 else float ('-infinity')
            bRight = b[rem+1] if (rem+1)<len(b) else float ('infinity')

            if aLeft <= bRight and bLeft <= aRight:
                if total % 2:
                    return min(aRight, bRight)
                else:
                    return (max(aLeft,bLeft) + min(aRight, bRight)) / 2

            elif aLeft > bRight:
                r = m - 1
            else:
                l = m + 1
