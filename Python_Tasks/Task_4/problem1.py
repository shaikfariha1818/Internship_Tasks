
# Problem: Python If-Else
# HackerRank: https://www.hackerrank.com/challenges/py-if-else/problem

n = int(input())

if n % 2 != 0:
    print("Weird")
elif n <= 5:
    print("Not Weird")
elif n <= 20:
    print("Weird")
else:
    print("Not Weird")
