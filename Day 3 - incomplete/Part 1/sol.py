import numpy as np

file = open('input.txt')
file = file.read()
file = file.strip().split('\n')
digit = [1,2,3,4,5,6,7,8,9,0]

for line in file:
    for x in range(len(line)):
        #print(line[x],line[x+1],line[x+2])
        if line[x].isdigit():
            if line[x+1].isdigit():
                if line[x+2].isdigit():
                    line[x] = line[x].replace('%d','.')
                    print(line)



#test = []
#test += [list(row) for row in file]
#symbols = set(['+','*','@','/','%','&','$','=','-','#'])
#total = 0

#for line in test:
#    print(test)

#print(total) 




