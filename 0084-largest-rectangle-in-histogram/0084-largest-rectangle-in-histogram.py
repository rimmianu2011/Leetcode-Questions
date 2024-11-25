class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, top = stack.pop()
                a = top * (i - index)
                max_area = max(max_area, a)
                start = index
            stack.append([start, h])

        while stack:
            index, top = stack.pop()
            a = top * (len(heights) - index)
            max_area = max(max_area, a)
    
        return max_area