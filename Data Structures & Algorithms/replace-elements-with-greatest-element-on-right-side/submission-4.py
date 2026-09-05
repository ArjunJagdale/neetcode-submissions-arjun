class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1] * len(arr)
        rmax = -1
        for i in range(len(arr)-1, -1, -1):
            res[i] = rmax
            rmax = max(rmax, arr[i])
        
        return res
        