class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm = {num:i for i, num in enumerate(nums1)}
        res = [-1] * len(nums1)

        for x in range(len(nums2)):
            if nums2[x] in hm:
                idx = 1
                while (idx+x<len(nums2)) and (nums2[idx+x] < nums2[x]):
                    idx += 1
                if idx+x < len(nums2):
                    res[hm[nums2[x]]] = nums2[idx+x]
        
        return res
