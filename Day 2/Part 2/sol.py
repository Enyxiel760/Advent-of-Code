import regex as re
list = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green','Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue']
result = 0
with open('input.txt') as f:
    for line in f:
    #for line in list:

        #split line into 2 strings, game id and results
        line = line.split(':')

        #trim game id list value to only contain digits
        for char in line[0]:
            if not char.isdigit():
                line[0] = line[0][1:]

        #initialize highest value
        x, y, z = 0, 0, 0
        
        #check for green
        for count,char in enumerate(line[1]):
            if line[1][count:].startswith('green'):
                #when we find 'green', look backwards 3 spaces (-3), as space before word and upto 2 digits,
                #and stop search at space before word(-1). if number is bigger than previous best, replace previous best with number
                if int(line[1][count-3:count-1]) > x:
                    x = int(line[1][count-3:count-1])

        #check for red
        for count,char in enumerate(line[1]):
            if line[1][count:].startswith('red'):
                if int(line[1][count-3:count-1]) > y:
                    y = int(line[1][count-3:count-1])

        #check for blue
        for count,char in enumerate(line[1]):
            if line[1][count:].startswith('blue'):
                if int(line[1][count-3:count-1]) > z:
                    z = int(line[1][count-3:count-1])
                    
        #add together the multiplication of the highest value for each color found            
        result += x*y*z
    print(result)