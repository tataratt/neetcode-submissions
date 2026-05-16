class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        if len(temperatures) == 1:
            return [0]
        
        res = [0] * len(temperatures)

        stack = [(temperatures[0], 0)]

        for i in range(1, len(temperatures)):
            ct = temperatures[i]
            while stack:
                if stack[-1][0] >= ct:
                    break
                
                pt, idx = stack.pop()

                res[idx] = i - idx
            stack.append((ct, i))

        return res
            