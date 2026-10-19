# Problem 20: Super Reduced String
# https://www.hackerrank.com/challenges/reduced-string/problem

s = input().strip()
stack = []

for c in s:
    if stack and stack[-1] == c:
        stack.pop()
    else:
        stack.append(c)

result = "".join(stack)
print(result if result else "Empty String")
