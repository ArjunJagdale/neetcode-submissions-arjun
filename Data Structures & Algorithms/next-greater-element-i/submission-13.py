class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = {}
        res = [-1] * len(nums1)
        
        # store index value pair
        for i, n in enumerate(nums1):
            h[n] = i
        
        print(h)
        # check next greater
        for i in range(len(nums2)-1):
            if nums2[i] in h:
                idx = 1
                while i+idx < len(nums2) and not nums2[i+idx] > nums2[i]:
                    idx += 1
                if i + idx < len(nums2):
                    res[h[nums2[i]]] = nums2[i+idx]
        return res 