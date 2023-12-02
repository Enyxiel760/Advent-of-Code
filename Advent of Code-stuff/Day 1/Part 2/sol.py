running = 0
valid = ['1','2','3','4','5','6','7','8','9']
#test = ['two1nine','eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']
#test = ['one','two','three','four','five','six','seven','eight','nine','1','2','3','4','5','6','7','8','9']
#test = ['three7jrgevfoureightwo4gulf']
with open('input.txt') as f:
    for line in f:
    #for line in test:
        temp_str = ''
        temp = line
        while len(temp) > 0:
            if temp[0] in valid:
                temp_str += str(temp[0])
                temp = temp[1:]

            elif len(temp) > 2 and temp[0] == 'o':
                if temp[1] == 'n':
                    if temp[2] == 'e':
                        temp = temp[1:]
                        temp_str += '1'
                    else:
                        temp = temp[1:]
                else:
                    temp = temp[1:]

            elif len(temp) > 2 and temp[0] == 't':
                if temp[1] == 'w':
                    if temp[2] == 'o':
                        temp = temp[1:]
                        temp_str += '2'
                    else:
                        temp = temp[1:]

                elif len(temp) > 3 and temp[1] == 'h':
                    if temp[2] == 'r':
                        if temp[3] == 'e':
                            if temp[4] == 'e':
                                temp = temp[1:]
                                temp_str += '3'
                            else:
                                temp = temp[1:]
                        else:
                            temp = temp[1:]
                    else:
                        temp = temp[1:]
                else:
                    temp = temp[1:]

            elif len(temp) > 3 and temp[0] == 'f':
                if temp[1] == 'o':
                    if temp[2] == 'u':
                        if temp[3] == 'r':
                            temp = temp[1:]
                            temp_str += '4'
                        else:
                            temp = temp[1:]
                    else:
                        temp = temp[1:]

                elif len(temp) > 3 and temp[1] == 'i':
                    if temp[2] == 'v':
                        if temp[3] == 'e':
                            temp = temp[1:]
                            temp_str += '5'
                        else:
                            temp = temp[1:]
                    else:
                        temp = temp[1:]
                else:
                    temp = temp[1:]

            elif len(temp) > 2 and temp[0] == 's':
                if temp[1] == 'i':
                    if temp[2] == 'x':
                        temp = temp[1:]
                        temp_str += '6'
                    else:
                        temp = temp[1:]

                elif len(temp) > 4 and temp[1] == 'e':
                    if temp[2] == 'v':
                        if temp[3] == 'e':
                            if temp[4] == 'n':
                                temp = temp[1:]
                                temp_str += '7'
                            else:
                                temp = temp[1:]
                        else:
                            temp = temp[1:]
                    else:
                        temp = temp[1:]
                else:
                    temp = temp[1:]

            elif len(temp) > 4 and temp[0] == 'e':
                if temp[1] == 'i':
                    if temp[2] == 'g':
                        if temp[3] == 'h':
                            if temp[4] == 't':
                                temp = temp[1:]
                                temp_str += '8'
                            else:
                                temp = temp[1:]
                        else:
                            temp = temp[1:]
                    else:
                        temp = temp[1:]
                else:
                    temp = temp[1:]

            elif len(temp) > 3 and temp[0] == 'n':
                if temp[1] == 'i':
                    if temp[2] == 'n':
                        if temp[3] == 'e':
                            temp = temp[1:]
                            temp_str += '9'
                        else:
                            temp = temp[1:]
                    else:
                        temp = temp[1:]
                else:
                    temp = temp[1:]
            else:
                temp = temp[1:]
            #print(temp_str)
        if len(temp_str) > 0:   
            running += int(temp_str[0] + temp_str[-1])
            #print(temp_str[0]+temp_str[-1])
        print(running)
print(running)
                
