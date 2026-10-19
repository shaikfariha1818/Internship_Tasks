# Problem 3: Mars Exploration
# https://www.hackerrank.com/challenges/mars-exploration/problem

s = input().strip()
changed = 0

for i in range(len(s)):
    if s[i] != "SOS"[i % 3]:
        changed += 1

print(changed)
