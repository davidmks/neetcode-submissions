class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_count = 1, 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                prod *= num

        res = [0] * len(nums)

        if zero_count > 1:
            return res

        for i, num in enumerate(nums):
            if zero_count:
                if num == 0:
                    res[i] = prod
                else:
                    res[i] = 0
            else:
                res[i] = prod // num
        return res
