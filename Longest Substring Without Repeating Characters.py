#Given a string s, find the length of the longest substring without repeating characters.

from collections import deque

s = "bdshkls8o3hj23ouvdsn987n" #example string

counter = 0
s_split = [*s]
temp = deque([])
for char in s_split:
    if char not in temp:
        temp.append(char)
        counter = max(counter, len(temp))
    else:
        while char in temp:
            temp.popleft()
        temp.append(char)



