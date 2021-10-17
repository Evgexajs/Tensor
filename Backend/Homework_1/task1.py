string = input()
even = 0
odd = 0
for symbol in string:
    number = int(symbol)
    if number % 2 == 0:
        even += number
    else:
        odd += number
print(odd, even)