class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        grt = -1
        op = [0] * len(arr)

        for i in range(len(arr)-1, -1, -1):
            op[i] = grt
            grt = max(grt, arr[i])
        
        return op