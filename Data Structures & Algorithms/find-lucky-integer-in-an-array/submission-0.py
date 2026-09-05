class Solution:
    def findLucky(self, arr: List[int]) -> int:
        h = {}
        largest = -1
        for i in arr:
            h[i] = h.get(i, 0 ) + 1 # {2:2, 3:1, 4:1}
        
        for i in range(len(arr)-1, -1, -1):
            if h[arr[i]] == arr[i] and arr[i] > largest:
                largest = arr[i]
        
        return largest