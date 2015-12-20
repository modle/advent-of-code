ribbon_length = 0
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

        elif x_count == 2 and w == 0:
            w = int(line[first_x+1:char_line_count])
            h = int(line[char_line_count+1:line_end])

        char_line_count += 1

    perim_1 = 2*(l+w)
    perim_2 = 2*(w+h)
    perim_3 = 2*(h+l)
    volume = l*w*h

    ribbon_length += min(perim_1, perim_2, perim_3) + volume

    line_count += 1

print (ribbon_length)
