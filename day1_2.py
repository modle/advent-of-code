floor_count = 0
char_count = 0

with open('day1_input.txt','r') as myfile:
    data = myfile.read()

for char in data:
    floor_count += (char == '(')
    floor_count -= (char == ')')
    char_count += 1

    if floor_count < 0:
        print (char_count)
        break
