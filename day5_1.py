data = open('day5_input.txt', 'r')

nice = 0

naughty_strings = ['ab', 'cd', 'pq', 'xy']
vowels = ['a', 'e', 'i', 'o', 'u']

for line in data:

    print line

    naughty = 0
    line_vowels = []
    char_pos = 1
    double_char = 0

    # if any naughty strings exist in the string, continue to next line
    for n in naughty_strings:
        if line.find(n) != -1:
            naughty = 1
            break

    if naughty == 1:
        print 'naughty'
        continue

    for char in line:
        # get unique list of vowels
        if char in vowels:
            line_vowels.append(char)

        # check for double chars
        if line[char_pos-1:1] == line[char_pos:1]:
            double_char = 1

        char_pos += 1

    if double_char == 1 and len(line_vowels) >= 3:
        print 'nice'
        print line_vowels
        nice += 1
        continue

print nice

# 568 is too high