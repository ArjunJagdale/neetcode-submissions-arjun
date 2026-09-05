class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = [[] for i in range(len(nums))]

        hm = {}
        for i in nums:
            hm[i] = hm.get(i, 0) + 1

        for i in hm:
            mapping[hm[i]-1].append(i)

        res = []
        for i in range(len(mapping)-1, -1, -1):
            if mapping[i] and k:
                x = len(mapping[i])
                while x:
                    res.append(mapping[i][x-1])
                    x -= 1
                    k -= 1
        
        return res