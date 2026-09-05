class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}

        for i in nums:
            h[i] = h.get(i, 0) + 1
        
        l = list(h.items())

        for i in range(len(l)):
            for j in range(i+1, len(l)):
                if l[j][1] > l[i][1]:
                    l[i], l[j] = l[j], l[i]
        
        res = []

        for i in range(k):
            res.append(l[i][0])
        
        return res
        

        
        