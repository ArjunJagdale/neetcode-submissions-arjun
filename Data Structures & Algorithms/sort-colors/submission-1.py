class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3

        for c in nums:
            count[c] += 1

        index = 0

        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[index] = i
                index += 1

        # def mergeSort(nums):

        #     if len(nums) <= 1:
        #         return nums

        #     mid = len(nums) // 2
        #     left = mergeSort(nums[:mid])
        #     right = mergeSort(nums[mid:])

        #     return merge(left, right)
        
        # def merge(left, right):
        #     result = []
        #     i = j = 0

        #     while i < len(left) and j < len(right):
        #         if left[i] < right[j]:
        #             result.append(left[i])
        #             i += 1
        #         else:
        #             result.append(right[j])
        #             j += 1
            
        #     result.extend(left[i:])
        #     result.extend(right[j:])

        #     return result
        
        # sorted_nums = mergeSort(nums)
        # for i in range(len(nums)):
        #     nums[i] = sorted_nums[i]
