class Solution:
    def rob(self, nums: List[int]) -> int:
        def house_robber(houses):
            memo = {}

            def best(i: int) -> int:
                if i < 0:
                    return 0
                if i in memo:
                    return memo[i]
                memo[i] = max(
                    best(i - 1),  # skip
                    best(i - 2) + houses[i],  # rob
                )
                return memo[i]

            return best(len(houses) - 1)

        if len(nums) == 1:
            return nums[0]
        return max(house_robber(nums[1:]), house_robber(nums[:-1]))

    #     n = len(nums)
    #     if n == 1:
    #         return nums[0]
    #     return max(self.rob_line(nums, 0, n - 1), self.rob_line(nums, 1, n))

    # def rob_line(self, nums: List[int], start: int, end: int) -> int:
    #     rob1, rob2 = 0, 0
    #     for i in range(start, end):
    #         rob1, rob2 = rob2, max(nums[i] + rob1, rob2)
    #     return rob2
