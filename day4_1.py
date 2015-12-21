import hashlib

p = 'yzbqklnj'

x = 0

while 1:
    hash_input = p + str(x)

    hash_output = hashlib.md5(hash_input).hexdigest()

    if hash_output[0:5] == '00000':
        print hash_output
        print x
        break

    else:
        x += 1
