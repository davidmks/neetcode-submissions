class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 2. solution (deque)
        dq = deque()
        output = []
        for i, num in enumerate(nums):
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            dq.append(i)

            if dq[0] <= i - k:
                dq.popleft()

            if i >= k - 1:
                output.append(nums[dq[0]])
        return output
        
        # # 1. solution (naive)
        # output = []
        # left = 0
        # window = []
        # for right, num in enumerate(nums):
        #     window.append(num)
        #     if len(window) == k:
        #         output.append(max(window))
        #         window.pop(len(window) - k)
        # return output
