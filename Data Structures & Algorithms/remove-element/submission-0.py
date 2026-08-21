class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 1. solution (k pointer)
        keep = 0
        for num in nums:
            if num != val:
                nums[keep] = num
                keep += 1
        return keep

        # # 2. solution
        # kept = len(nums)
        # i = 0
        # while i < kept:
        #     if nums[i] == val:
        #         kept -= 1
        #         nums[i] = nums[kept] # dont advance i; pulled needs recheck
        #     else:
        #         i += 1
        # return kept


