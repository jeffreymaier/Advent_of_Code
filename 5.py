X = [l.strip() for l in open('5.in')]

one = ['S', 'L', 'W']
two = ['J', 'T', 'N', 'Q']
three = ['S', 'C', 'H', 'F', 'J']
four = ['T', 'R', 'M', 'W', 'N', 'G', 'B']
five = ['T', 'R', 'L', 'S', 'D', 'H', 'Q', 'B']
six = ['M', 'J', 'B', 'V', 'F', 'H', 'R', 'L']
seven = ['D', 'W', 'R', 'N', 'J', 'M']
eight = ['B', 'Z', 'T', 'F', 'H', 'N', 'D', 'J']
nine = ['H', 'L', 'Q', 'N', 'B', 'F', 'T']

stacks = {
    1 : one,
    2 : two,
    3 : three,
    4 : four,
    5 : five,
    6 : six,
    7 : seven,
    8 : eight,
    9 : nine,
}

for i in X:
    x = i.replace("move ", '').replace(" from ", ' ').replace(" to ", ' ')

    ranges = [(map(int, x.split(' ')))]
    a, b, c = ranges[0]

    # Solution for part 1
    #for n in range(a):
    #    stacks[c].append(stacks[b][-1]) 
    #    del stacks[b][-1]
       # stacks[b].pop(-a:)

    # Solution for part 2
    while a > 0:
        stacks[c].append(stacks[b][-a])
        del stacks[b][-a]
        a -= 1

for crate in stacks:
    print(stacks[crate][-1])

