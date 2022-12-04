# Part 1
with open('input.txt', 'r') as f:
    content = f.readlines()
    priorities = []
    for rucksack in content:
        firstpart, secondpart = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        common = list(set(firstpart) & set(secondpart))[0]
        priorities.append(ord(common) - 96 if common.islower() else ord(common) - 38)
    print(sum(priorities))

# Part 2
with open('input2.txt', 'r') as f:
    content = f.readlines()
    priorities = []
    for i in range(0, len(content), 3):
        group = content[i:i+3]
        common = list(set(group[0].rstrip('\n')) & set(group[1].rstrip('\n')) & set(group[2].rstrip('\n')))[0]
        priorities.append(ord(common) - 96 if common.islower() else ord(common) - 38)
    print(sum(priorities))