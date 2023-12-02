import regex as re
nums = ['one','two','three','four','five','six','seven','eight','nine']
sum = 0
with open('input.txt') as f:
    for line in f:
        x = re.findall('one|two|three|four|five|six|seven|eight|nine|\\d', line, overlapped=True )
        for i in x:
            for index in range(len(nums)):
                if i == nums[index]:
                    x[x.index(i)] = str(index+1)
        sum += int(x[0] + x[-1])
    print(sum)
    