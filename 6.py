message = list(open("6.in").read())

# print(message)

# ** Part 1 start
x = 0
y = 4
message_start = 4


for i in message:
    check = message[x:y]
    if len(check) == len(set(check)):
        print(message_start)
        break
    else:
        x += 1
        y += 1
        message_start += 1

# Part 1 end **