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

        # ---

        # # solution 3 (hash)
        # streaks: dict[int, int] = {}
        # longest = 0

        # for num in nums:
        #     if num in streaks:
        #         continue  # already placed, which also skips duplicates

        #     left = streaks.get(num - 1, 0)
        #     right = streaks.get(num + 1, 0)
        #     streak = left + right + 1

        #     streaks[num - left] = streak
        #     streaks[num + right] = streak
        #     streaks[num] = streak

        #     longest = max(longest, streak)

        # return longest

        # ---

        # # solution 1 (sort)
        # if not nums:
        #     return 0

        # ordered = sorted(set(nums))
        # longest = streak = 1
        # for i in range(1, len(ordered)):
        #     if ordered[i] == ordered[i - 1] + 1:
        #         streak += 1
        #     else:
        #         streak = 1
        #     longest = max(longest, streak)
        # return longest
