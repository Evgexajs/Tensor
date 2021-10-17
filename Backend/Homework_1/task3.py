current = 50
left = 1
right = 100
print(current)
string = input()
while (string != 'Верно'):
    if (string == 'Больше'):
        left = current
        current = int((left + right) / 2)
    else:
        right = current
        current = int((left + right) / 2)
    print(current)
    string = input()