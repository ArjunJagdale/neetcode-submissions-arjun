class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Merge Sort
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

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
        
        # Actual code
        s = mergeSort(s)
        g = mergeSort(g)

        i, j = 0, 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1
        
        return i