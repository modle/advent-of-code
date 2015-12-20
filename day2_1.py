total_sq_ft = 0
line_count = 0
sq_ft = 0

data = open('day2_input.txt','r')

for line in data:
    x_count = 0
    char_line_count = 0
    l = 0
    w = 0
    h = 0
    first_x = 0
    break_pos = 0
    line_end = 0

    for char in line:
        break_pos += (char == '\n')
        if break_pos == 1:
            break
        line_end += 1

    for char in line:
        x_count += (char == 'x')

        if x_count == 1 and l == 0:
            l = int(line[0:char_line_count])
            first_x = char_line_count
            # print ('first x', first_x)
        elif x_count == 2 and w == 0:
            w = int(line[first_x+1:char_line_count])
            h = int(line[char_line_count+1:line_end])

        char_line_count += 1

    surf_1 = l*w
    surf_2 = w*h
    surf_3 = h*l

    total_sq_ft += 2*(surf_1 + surf_2 + surf_3) + min (surf_1, surf_2, surf_3)

    line_count += 1

print (total_sq_ft)
