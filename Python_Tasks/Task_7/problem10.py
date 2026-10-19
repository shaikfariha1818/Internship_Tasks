# Problem 10: CamelCase
# https://www.hackerrank.com/challenges/camelcase/problem

s = input().strip()

if s:
    print(1 + sum(c.isupper() for c in s))
else:
    print(0)
