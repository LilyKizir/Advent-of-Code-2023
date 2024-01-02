with open('input.txt') as f:
    sum = 0
    for line in f:

        addend = ''

        for char in line:
            if char.isdigit() == False:
                continue
            addend += char
            break
        for char in reversed(line):
            if char.isdigit() == False:
                continue
            addend += char
            break
        sum += int(addend)
    print("Calibration sum: ",sum)
