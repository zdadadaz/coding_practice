class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            nums1[:] = nums2[:]
            return
        pt1 = m-1
        pt2 = n-1
        tot = len(nums1)-1
        pt1m = tot
        while pt1 > -1 and pt2 > -1:
            if nums1[pt1] < nums2[pt2]:
                nums1[pt1m] = nums2[pt2]
                pt2-=1
            else:
                nums1[pt1m] = nums1[pt1]
                pt1 -=1
            pt1m-=1
        while pt1>-1:
            nums1[pt1m] = nums1[pt1]
            pt1m-=1
            pt1-=1
        while pt2>-1:
            nums1[pt1m] = nums2[pt2]
            pt1m-=1
            pt2-=1