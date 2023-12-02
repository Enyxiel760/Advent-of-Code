import regex as re
list = ['test']

with open('input.txt') as f:
    for line in f:

        #split line into 2 strings, game id and results
        line = line.split(':')

        #trim game id list value to only contain digits
        for char in line[0]:
            if not char.isdigit():
                line[0] = line[0][1:]

        #initialize
        x, y, z = True, True, True
        
        #check for green
        for count,char in enumerate(line[1]):
            if line[1][count:].startswith('green'):
                #when we find 'green', look backwards 3 spaces (-3), as space before word and upto 2 digits,
                #and stop search at space before word(-1). if more than permissible set flag False
                if int(line[1][count-3:count-1]) > 13:
                    x = False

        #check for red
        for count,char in enumerate(line[1]):
            if line[1][count:].startswith('red'):
                if int(line[1][count-3:count-1]) > 12:
                    y = False

        #check for blue
        for count,char in enumerate(line[1]):
            if line[1][count:].startswith('blue'):
                if int(line[1][count-3:count-1]) > 14:
                    z = False

        #if no flags have been set false, game is valid, add game id contained in [0] to list
        if x == True and y == True and z == True:
            list.append(re.search('[0-9]*', line[0]))

result = 0
#list contains match objects and so this is just a standard loop, modified to add the match values together
for i in range(1,len(list)):
    result += int(list[i].group())
print(result)