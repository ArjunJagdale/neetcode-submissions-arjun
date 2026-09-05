class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]

            sortedleft = mergeSort(left)
            sortedright = mergeSort(right)

            return merge(sortedleft, sortedright)
        
        def merge(left, right):
            i = j = 0
            rs = []

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    rs.append(left[i])
                    i += 1
                else:
                    rs.append(right[j])
                    j += 1
            
            rs.extend(left[i:])
            rs.extend(right[j:])

            return rs
        
        result = mergeSort(nums)
        return result