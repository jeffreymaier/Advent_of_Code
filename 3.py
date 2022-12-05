values = {
    'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12, 'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16, 'q' : 17, 'r' : 18, 's' : 19, 't' : 20, 'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24, 'y' : 25, 'z' : 26,
    'A' : 27, 'B' : 28, 'C' : 29, 'D' : 30, 'E' : 31, 'F' : 32, 'G' : 33, 'H' : 34, 'I' : 35, 'J' : 36, 'K' : 37, 'L' : 38, 'M' : 39, 'N' : 40, 'O' : 41, 'P' : 42, 'Q' : 43, 'R' : 44, 'S' : 45, 'T' : 46, 'U' : 47, 'V' : 48, 'W' : 49, 'X' : 50, 'Y' : 51, 'Z' : 52,
}

X = [l.strip() for l in open('3.in')]
""" Part 1 
value = 0
for i in X:
    t = [*i]
    u = int(len(t) / 2)

    first = t[0:u]
    second = t[u:]
    same = list(set(first) & set(second))
    value += values[same[0]]
    print(value)
 """
x = 0
y = 1
z = 2
badge_values = 0
for n in range(100):
    elf_1 = X[x]
    elf_2 = X[y]
    elf_3 = X[z]
    badge = list( set(elf_1) & set(elf_2) & set(elf_3))
    badge_values += values[badge[0]]
    x += 3
    y += 3
    z += 3

print(badge_values)