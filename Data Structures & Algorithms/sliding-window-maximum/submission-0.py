class Solution:
    import heapq
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        hq = []
        heapq.heapify(hq)
        l = 0
        res = []

        for r in range(len(nums)):
            heapq.heappush(hq, (-nums[r], r))

            if r - l + 1 == k:
                while hq:
                    n, i = heapq.heappop(hq)
                    if l <= i <= r:
                        res.append(-n)
                        heapq.heappush(hq, (n, i))
                        break
                l += 1
        return res