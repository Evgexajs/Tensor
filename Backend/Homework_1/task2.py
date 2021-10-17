age = int(input())
t1 = age % 10
t2 = age % 100
if (t1 == 1 and t2 != 11):
    print(age, 'год')
elif (t1 >= 2 and t1 <= 4 and (t2 < 10 or t2 >= 20)):
    print(age, 'года')
else:
    print(age, 'лет')