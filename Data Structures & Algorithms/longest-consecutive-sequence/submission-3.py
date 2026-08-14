class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # solution 2 (set)
        seen = set(nums)
        longest = 0

        for num in nums:
            if num - 1 in seen:
                continue  # not the smallest element
            streak = 1
            while num + streak in seen:
                streak += 1
            longest = max(longest, streak)
        return longest

        # # solution 1 (sort)
        # if not nums:
        #     return 0

        # ordered = sorted(set(nums))
        # best = current = 1

        # for i in range(1, len(ordered)):
        #     if ordered[i] == ordered[i - 1] + 1:
        #         current += 1
        #     else:
        #         current = 1
        #     best = max(best, current)

        # return best
