import regex as re
points = 0

with open('input.txt') as f:
    for line in f:
        line.strip()
        list = re.split('   |  | |:  |: | \|  | \| |\n', line)
        count =-1
        temp = 0
        for item in list[-26:-1]:
            if item in list[2:12]:
                temp = 1
                count += 1
        points += temp*(2**count)
print(points)