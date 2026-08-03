class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        totalLength = len(nums1) + len(nums2)
        halfLength = totalLength // 2

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        l , r = 0, len(nums1) - 1

        while True:
            i_nums1 = (l + r) // 2
            j_nums2 = halfLength - (i_nums1 + 1) - 1

            nums1Left = nums1[i_nums1] if i_nums1>=0 else float("-infinity")
            nums1Right = nums1[i_nums1 + 1] if (i_nums1+1) < len(nums1) else float("infinity")

            nums2Left = nums2[j_nums2] if j_nums2 >=0 else float("-infinity")
            nums2Right = nums2[j_nums2 + 1] if (j_nums2 + 1) < len(nums2) else float("infinity")

            if nums1Left <= nums2Right and nums2Left <= nums1Right:
                if totalLength % 2:
                    return min(nums1Right, nums2Right)
                return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2
            elif nums1Left > nums2Right:
                r = i_nums1 - 1
            else:
                l = i_nums1 + 1
