running = 0
with open('input.txt') as f:
    for line in f:
        temp = []
        for x in line:
            if x.isdigit():
                temp.append(x)
        running += int(temp[0] + temp[-1])
print(running)


