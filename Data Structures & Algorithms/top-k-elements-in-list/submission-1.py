class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        result = []

        for _ in range(k):
            max_key = max(count, key = count.get)
            result.append(max_key)
            del count[max_key]
        
        return result
        

        
        