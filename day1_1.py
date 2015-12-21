count = 0

with open('day1_input.txt', 'r') as myfile:
    data = myfile.read()

for char in data:
    count += (char == '(')
    count -= (char == ')')

print (count)
