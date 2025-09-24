# Longest valid parentheses
# https://www.geeksforgeeks.org/problems/longest-valid-parentheses5657/1



def longestValidParentheses(s):
    stack = [-1] 
    max_len = 0

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else: 
            stack.pop()
            if not stack:
                stack.append(i) 
            else:
                max_len = max(max_len, i - stack[-1])

    return max_len

s1 = "((()"
s2 = ")()())"
s3 = "())()"

print(longestValidParentheses(s1)) 
print(longestValidParentheses(s2))  
print(longestValidParentheses(s3))  
