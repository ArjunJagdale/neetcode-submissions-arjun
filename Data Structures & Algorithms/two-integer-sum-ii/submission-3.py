class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h_map = {}
        for i, n in enumerate(numbers):
            diff = target - n

            if diff in h_map:
                return [h_map[diff]+1, i+1]
            
            h_map[n] = i
        