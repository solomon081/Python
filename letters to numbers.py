input = raw_input('Write Text: ')
input = input.lower()
output = []
for character in input:
    number = ord(character) - 96
    output.append(number)
print output
