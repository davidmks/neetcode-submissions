class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 2. solution (hash - 1 pass)
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        # ---

        # # 1. solution (hash - 2 pass)
        
        # index_of = {num: i for i, num in enumerate(nums)}

        # for i, num in enumerate(nums):
        #     complement = target - num
        #     if complement in index_of and index_of[complement] != i:
        #         return [i, index_of[complement]]
