class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        index = -1

        for i in range(len(arr)-1,-1,-1):
            res[i] = index
            index = max(index, arr[i])
        
        return res