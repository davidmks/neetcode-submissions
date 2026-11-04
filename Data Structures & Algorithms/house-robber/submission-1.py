class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1, rob2 = 0, 0
        # for n in nums:
        #     rob1, rob2 = rob2, max(rob1 + n, rob2)
        # return rob2

        memo = {}

        def best(i: int) -> int:
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[i], nums[i - 1])
            if i in memo:
                return memo[i]
            memo[i] = max(
                best(i - 1),  # skip
                best(i - 2) + nums[i],  # rob
            )
            return memo[i]

        return best(len(nums) - 1)
