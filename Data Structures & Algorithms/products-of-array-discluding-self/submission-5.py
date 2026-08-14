class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_count = 1, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            else:
                prod *= nums[i]
        output = [0] * len(nums)
        if zero_count > 1:
            return output

        for i in range(len(nums)):
            if zero_count > 0:
                pass
                output[i] = prod if nums[i] == 0 else 0
            else:
                output[i] = prod // nums[i]
        return output