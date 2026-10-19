# Problem 4: Funny String
# https://www.hackerrank.com/challenges/funny-string/problem

def funnyString(s):
    values = [ord(c) for c in s]
    reverse_values = values[::-1]

    for i in range(1, len(values)):
        if abs(values[i] - values[i - 1]) != abs(
            reverse_values[i] - reverse_values[i - 1]
        ):
            return "Not Funny"

    return "Funny"


t = int(input())
for _ in range(t):
    s = input().strip()
    print(funnyString(s))
