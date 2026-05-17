class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []

        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] >= h:
                idx, height = stack.pop()
                maxArea = max(maxArea, height * (i - idx))
                start = idx
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (n - i))
            

        return maxArea