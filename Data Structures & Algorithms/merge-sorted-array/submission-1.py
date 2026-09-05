class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]
            
            sortedLeft = mergeSort(left)
            sortedRight = mergeSort(right)
            
            return merge(sortedLeft, sortedRight)
        
        def merge(left, right):
            i = j = 0
            res = []
            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            
            res.extend(left[i:])
            res.extend(right[j:])
            
            return res 

        nums1[:] = mergeSort(nums1)   
        

        