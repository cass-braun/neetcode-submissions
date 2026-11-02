class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()  # stores indices of elements
        l = 0

        for r in range(len(nums)):
            # 1. Remove elements from the back that are smaller than the current element
            # (They can never be the maximum since a larger, newer element is here)
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            # 2. Add the current element's index
            q.append(r)

            # 3. Remove the front element if it has fallen out of the current window
            if l > q[0]:
                q.popleft()

            # 4. Once we reach window size k, add the max (at the front of the queue) to results
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1  # Slide the left pointer forward
                
        return res