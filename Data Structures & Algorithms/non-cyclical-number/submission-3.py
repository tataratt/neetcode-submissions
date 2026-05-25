class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        total = 0
        cur = n
        while total != 1:
            total = 0
            for ch in str(cur):
                total += int(ch) * int(ch)

            if total in seen:
                return False
            seen.add(total)
            cur = total

        return True
            