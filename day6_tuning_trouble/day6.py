from collections import deque

input_string = open("input.txt").read()
characters = deque()

# Part 1 - {4}
for i, character in enumerate(input_string):
    characters.appendleft(character)
    if len(characters) < 4: continue

    if len(set(characters)) == 4:
        print(i + 1) # answer
        break
    characters.pop()

# Part 2 - {14}
for i, character in enumerate(input_string):
    characters.appendleft(character)
    if len(characters) < 14: continue

    if len(set(characters)) == 14:
        print(i + 1)
        break
    characters.pop()