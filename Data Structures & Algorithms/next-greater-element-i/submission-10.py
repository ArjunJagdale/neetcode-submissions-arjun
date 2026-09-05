class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = {num:i for i, num in enumerate(nums1)}

        res = [-1] * len(nums1)
        for i in range(len(nums2)): # 0 to 3 | 1, 3, 4, 2
            if nums2[i] in h: # yes 1 in h
                for j in range(i+1, len(nums2)): # if 1 in h, then start from 3 up to 2 | 1 to 3
                    if nums2[j] > nums2[i]:
                        idx = h[nums2[i]] # pick index of i for the nums1 from h
                        res[idx] = nums2[j]
                        break
        return res