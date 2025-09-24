# Largest rectangle in histogram
# https://www.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram-1587115620/1



def largestRectangleArea(arr):
    stack = []
    max_area = 0
    n = len(arr)
    
    for i in range(n + 1):
        h = 0 if i == n else arr[i]
        while stack and arr[stack[-1]] > h:
            height = arr[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area

arr1 = [60, 20, 50, 40, 10, 50, 60]
arr2 = [3, 5, 1, 7, 5, 9]
arr3 = [3]

print(largestRectangleArea(arr1))  
print(largestRectangleArea(arr2))  
print(largestRectangleArea(arr3))  
