class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 2. solution (prefix & suffix)
        n = len(nums)
        output = [0] * n

        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in reversed(range(n)):
            output[i] *= suffix
            suffix *= nums[i]
        return output

        # # 1. solution (division)
        # prod, zero_count = 1, 0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         zero_count += 1
        #     else:
        #         prod *= nums[i]

        # output = [0] * len(nums)
        # if zero_count > 1:
        #     return output

        # for i in range(len(nums)):
        #     if zero_count > 0:
        #         output[i] = prod if nums[i] == 0 else 0
        #     else:
        #         output[i] = prod // nums[i]
        # return output