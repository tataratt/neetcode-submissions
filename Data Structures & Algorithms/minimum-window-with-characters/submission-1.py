class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}
        l = 0

        for c in t:
            count[c] = 1 + count.get(c, 0)  
        
        res = ""
        cur = len(t)

        for r in range(len(s)):
            print(l, r, cur)
            if s[r] in count:
                count[s[r]] -= 1
                if count[s[r]] >= 0:
                    cur -= 1
            
            if cur == 0:
                while l < r:
                    if s[l] in count:
                        if count[s[l]] == 0:
                            break
                        count[s[l]] += 1
                    l += 1
                if not res or r - l + 1 < len(res):
                    res = s[l:r+1]

                if s[l] in count:
                    count[s[l]] += 1
                    if count[s[l]] > 0:
                        cur += 1
                l += 1

        return res