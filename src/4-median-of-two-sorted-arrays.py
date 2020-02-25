'''https://leetcode.com/problems/median-of-two-sorted-arrays/'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        '''ensuring len(nums1) is lesser'''
        if m>n:
            return self.findMedianSortedArrays(nums2, nums1)
        
        l, h = 0, m
        while l<=h:
            partitionX = (l+h)//2
            partitionY = (m+n+1)//2 - partitionX
            
            maxLeft1 = float('-inf') if partitionX==0 else nums1[partitionX-1]
            maxLeft2 = float('-inf') if partitionY==0 else nums2[partitionY-1]
            
            minRight1 = float('inf') if partitionX==m else nums1[partitionX]
            minRight2 = float('inf') if partitionY==n else nums2[partitionY]
            
            if maxLeft1<=minRight2 and maxLeft2<=minRight1:
                '''Result'''
                if (m+n)%2==0:  #even
                    return (max(maxLeft1, maxLeft2)+min(minRight1, minRight2))/2
                else:
                    return max(maxLeft1, maxLeft2)/1.0
            elif maxLeft1>minRight2:
                h = partitionX-1
            else:
                l = partitionX +1
        