class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        res = []
        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            nxt = digits[i] + carry

            res.append(nxt % 10)

            carry = 1 if nxt >= 10 else 0

        if carry:
            res.append(1)

        return res[::-1]