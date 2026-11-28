class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1

        m,n = len(nums1),len(nums2)

        l,r = 0,m
        while l <=r:
            i =(l + r)//2
            j =(m + n +1)//2 - i

            maxleft1 = float('-inf') if i ==0 else nums1[i - 1]
            minright1 = float('inf') if i == m else nums1[i]

            maxleft2 = float('-inf') if j == 0 else nums2[j - 1]
            minright2 = float('inf') if j == n else nums2[j]

            if maxleft1 <= minright2 and maxleft2 <= minright1:
                if (m + n)%2 == 1:
                    return max(maxleft1,maxleft2)
                return (max(maxleft1,maxleft2) + min(minright1,minright2))/2
            elif maxleft1 > minright2:
                r = i - 1
            else:
                l = i + 1