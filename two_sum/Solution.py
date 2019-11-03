class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, num in enumerate(nums):
            n = target - num
            if n not in d:
                d[num] = index
            else:
                return [d[n], index]

'''
Time complexity: O(n) 
'''