import regex as re
matches = []

with open('input.txt') as f:
    for line in f:
        line.strip()
        line = re.split('   |  | |:  |: | \|  | \| |\n', line)
        count =0
        for item in line[-26:-1]:
            if item in line[2:12]:
                count += 1
        matches.append(count)

totals = [1] * len(matches)

for id,item in enumerate(matches):
    for x in range(1,item+1):
        totals[id+x] += 1*totals[id] 
print(sum(totals))
