X = [l.strip() for l in open('2.in')]

scoring = {
        'A' : 1,
        'B' : 2,
        'C' : 3,
        'X' : 1,
        'Y' : 2,
        'Z' : 3,
        }


my_score = 0

for i in range(len(X)):
    game = X[i].split(' ')
    opp = game[0]
    me = game[1]
    if opp == 'A' and me == 'X':
        my_score += scoring[me] + 3
    elif opp == 'A' and me == 'Y':
        my_score += scoring[me] + 6
    elif opp == 'A' and me == 'Z':
        my_score += scoring[me]
    elif opp == 'B' and me == 'X':
        my_score += scoring[me]
    elif opp == 'B' and me == 'Y':
        my_score += scoring[me] + 3
    elif opp == 'B' and me == 'Z':
        my_score += scoring[me] + 6
    elif opp == 'C' and me == 'X':
        my_score += scoring[me] + 6
    elif opp == 'C' and me == 'Y':
        my_score += scoring[me]
    elif opp == 'C' and me == 'Z':
        my_score += scoring[me] + 3

print(my_score)

results = {
        'win' : {
            'A' : 'Y',
            'B' : 'Z',
            'C' : 'X',
            },
        'tie' : {
            'A' : 'X',
            'B' : 'Y',
            'C' : 'Z',
            },
        'lose' : {
            'A' : 'Z',
            'B' : 'X',
            'C' : 'Y',
            }
        }

needed_score = 0
for i in range(len(X)):
    game = X[i].split(' ')
    opp = game[0]
    if game[1] == 'X':
        me = results['lose'][opp]
        needed_score += scoring[me]
    elif game[1] == 'Y':
        me = results['tie'][opp]
        needed_score += scoring[me] + 3
    elif game[1] == 'Z':
        me = results['win'][opp]
        needed_score += scoring[me] + 6

print(needed_score)
























