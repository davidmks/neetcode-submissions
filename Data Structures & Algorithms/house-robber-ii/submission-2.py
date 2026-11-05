class Solution:
    def rob(self, nums: List[int]) -> int:
        def house_robber(houses):
            two_back, one_back = 0, 0
            for money in houses:
                two_back, one_back = one_back, max(one_back, money + two_back)
            return one_back

        if len(nums) == 1:
            return nums[0]
        return max(house_robber(nums[1:]), house_robber(nums[:-1]))

        # def house_robber(houses):
        #     memo = {}

        #     def best(i: int) -> int:
        #         if i < 0:
        #             return 0
        #         if i in memo:
        #             return memo[i]
        #         memo[i] = max(
        #             best(i - 1),  # skip
        #             best(i - 2) + houses[i],  # rob
        #         )
        #         return memo[i]

        #     return best(len(houses) - 1)

        # if len(nums) == 1:
        #     return nums[0]
        # return max(house_robber(nums[1:]), house_robber(nums[:-1]))
