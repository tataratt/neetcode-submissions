class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        def check(piles, k) -> int:
            res = 0
            for p in piles:
                res += math.ceil(p / k)
            
            return res

        ans = right

        while left <= right:
            mid = (left + right) // 2
            print(check(piles, mid))
            if check(piles, mid) <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans