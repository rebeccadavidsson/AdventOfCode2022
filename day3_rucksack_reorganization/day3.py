with open('input.txt', 'r') as content:
    priorities = []
    for rucksack in content:
        firstpart, secondpart = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        common = list(set(firstpart) & set(secondpart))[0]
        priorities.append(ord(common) - 96 if common.islower() else ord(common) - 38)
    print(sum(priorities))
