class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        res = []

        for i in range(1, len(arr)):
            large = max(arr[i:])
            res.append(large)
        
        res.append(-1)
        return res
        
        