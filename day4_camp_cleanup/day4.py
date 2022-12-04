with open('input.txt', 'r') as f:
    pairs = f.read().split('\n')

# Part 1
overlaps = 0
for pair in pairs:
    pair1, pair2 = pair.split(',')
    range1 = range(int(pair1.split('-')[0]),int(pair1.split('-')[1]))
    range2 = range(int(pair2.split('-')[0]),int(pair2.split('-')[1]))

    if range1.start <= range2.start and range1.stop >= range2.stop:
        overlaps += 1
        continue
    if range1.start >= range2.start and range1.stop <= range2.stop:
        overlaps += 1
        continue
print(overlaps)


# Part 2
overlaps = 0
for pair in pairs:
    pair1, pair2 = pair.split(',')
    range1 = range(int(pair1.split("-")[0]),int(pair1.split("-")[1]) + 1)
    range2 = range(int(pair2.split("-")[0]),int(pair2.split("-")[1]) + 1)

    if max(range1.start,range2.start) < min(range1.stop,range2.stop):
        overlaps += 1
print(overlaps)
