with open('4.in') as fin:
    lines = fin.read().strip().split()

#print(lines)

ans = 0

for line in lines:
    elves = line.split(",")
    ranges = [list(map(int, elf.split('-'))) for elf in elves]

    a, b = ranges[0]
    c, d = ranges[1]

    if a <= c and b >= d or a >= c and b <= d:
        ans += 1

print(ans)

pairs = 0
for line in lines:
    elves = line.split(",")
    ranges = [list(map(int, elf.split('-'))) for elf in elves]

    a, b = ranges[0]
    c, d = ranges[1]

    if a > d:
        continue
    elif b < c:
        continue
    else:
        pairs += 1

print(pairs)