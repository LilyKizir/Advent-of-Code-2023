import pdb
with open('input2.txt') as f:
    dictionary = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
    }
    sum = 0
    for line in f:

        length = len(line)
        addend = ''
        summand = ''

        for i, char in enumerate(line):
            if char.isdigit() == True:
                addend += char
                break

            if char not in "otfsen":
                continue

            if line[i:i+3] in dictionary:
                addend += str(dictionary[line[i:i+3]])
            elif line[i:i+4] in dictionary:
                addend += str(dictionary[line[i:i+4]])
            elif line[i:i+5] in dictionary:
                addend += str(dictionary[line[i:i+5]])

            if addend:
                break
        # print(addend)
        for i, char in enumerate(reversed(line)):
            if char.isdigit() == True:
                summand += char
                break

            if char not in "eorxnt":
                continue
            
            print(i)
            print(line[-i])
            if line[i:i+3][::-1] in dictionary:
                summand += str(dictionary[line[i:i+3][::-1]])
            elif line[i:i+4][::-1] in dictionary:
                summand += str(dictionary[line[i:i+4][::-1]])
            elif line[i:i+5][::-1] in dictionary:
                summand += str(dictionary[line[i:i+5][::-1]])

            if summand:
                break
        # print(summand)

        