class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        keys = list(hashmap.keys())
        values = list(hashmap.values())

        for i in range(len(values)):
            ind = i
            for j in range(i+1, len(values)):
                if values[j] > values[ind]:
                    ind = j
            # Swap
            values[i], values[ind] = values[ind], values[i]
            keys[i], keys[ind] = keys[ind], keys[i]
        
        return keys[:k]
