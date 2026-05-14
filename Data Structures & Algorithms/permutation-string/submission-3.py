class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        l_s1 = len(s1)
        l = 0
        maxf = 0

        for c in s1:
            count[c] = 1 + count.get(c, 0)

        for r in range(len(s2)):
            if s2[r] in count:
                count[s2[r]] -= 1
                if count[s2[r]] >= 0:
                    maxf += 1

            if maxf == l_s1:
                return True

            if r - l + 1 == l_s1:
                if s2[l] in count:
                    count[s2[l]] += 1
                    if count[s2[l]] > 0:
                        maxf -= 1
                l += 1

        return False

            