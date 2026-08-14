class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        
        # index_of = {num: i for i, num in enumerate(nums)}

        # for i, num in enumerate(nums):
        #     complement = target - num
        #     if complement in index_of and index_of[complement] != i:
        #         return [i, index_of[complement]]
