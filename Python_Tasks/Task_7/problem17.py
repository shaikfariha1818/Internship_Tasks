# Problem 17: Separate the Numbers
# https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separate_numbers(s):
    for i in range(1, len(s) // 2 + 1):
        first = s[:i]
        num = int(first)
        expected = first

        while len(expected) < len(s):
            num += 1
            expected += str(num)

        if expected == s:
            print("YES", first)
            return

    print("NO")


q = int(input())

for _ in range(q):
    s = input().strip()
    separate_numbers(s)
