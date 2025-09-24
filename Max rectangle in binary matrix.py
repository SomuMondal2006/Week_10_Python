# Max rectangle in binary matrix
# https://www.geeksforgeeks.org/problems/max-rectangle/1



def largestRectangleArea(heights):
    """Helper to compute largest rectangle in histogram"""
    stack = []
    max_area = 0
    heights.append(0) 

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    heights.pop() 
    return max_area


def maximalRectangle(mat):
    if not mat or not mat[0]:
        return 0

    n, m = len(mat), len(mat[0])
    heights = [0] * m
    max_area = 0

    for r in range(n):
        for c in range(m):
            if mat[r][c] == 1:
                heights[c] += 1
            else:
                heights[c] = 0
        max_area = max(max_area, largestRectangleArea(heights))

    return max_area


mat1 = [
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0]
]
print(maximalRectangle(mat1)) 

mat2 = [
    [0, 1, 1],
    [1, 1, 1],
    [0, 1, 1]
]
print(maximalRectangle(mat2))  
