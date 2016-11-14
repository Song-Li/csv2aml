f = open('input.csv', 'r')
cur = 0
pre = 'set ii := 1  2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38;\nset jj:=  1 2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33 34  35  36  37  38;\nparam sigma:  1 2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33 34  35  36  37  38:='

file_num = 0
out = open('./output/' + str(file_num) + '.dat', 'a')
out.write(pre + '\n')

for line in f:
    cur += 1
    if cur == 39:
        out.close()
        cur = 1
        file_num += 1
        out = open('./output/' + str(file_num) + '.dat', 'a')
        out.write(pre + '\n')

    nums = line.split(',')
    out.write(str(cur) + '\t')
    for num in nums:
        if cur == 38 and num[-1] == '\n':
            out.write(num[:-2])
            out.write(';\n')
        else:
            out.write(num)
            out.write(' ')

