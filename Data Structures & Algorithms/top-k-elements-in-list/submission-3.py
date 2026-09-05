class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        arr = []

        for i, num in count.items():
            arr.append([num, i])
        
        # sort function
        for i in range(len(arr)):
            idx = i
            for j in range(i+1, len(arr)):
                if arr[j] > arr[idx]:
                    idx = j
            (arr[i], arr[idx]) = (arr[idx], arr[i])
        
        return [sublist[1] for sublist in arr[:k]]
            

        

        
        