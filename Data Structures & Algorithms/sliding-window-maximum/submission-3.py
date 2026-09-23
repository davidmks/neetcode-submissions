class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 2. solution (deque)
        dq = deque()
        output = []
        for i in range(len(nums)):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)

            if dq[0] <= i - k:
                dq.popleft()

            if i >= k - 1:
                output.append(nums[dq[0]])
        return output

        # # naive approach
        # result = []
        # for right in range(k, len(nums) + 1):
        #     result.append(max(nums[right - k : right]))
        # return result
