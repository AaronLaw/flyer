filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()


with open(filename) as file_object:
    for line in lines:
        print(line.rstrip())
        file_object.write(lines)