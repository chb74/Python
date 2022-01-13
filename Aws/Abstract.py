
import datetime , pprint
name = 'Fred'
age = 50 

anniversary = datetime.date(1991, 10, 12)

a = f'My name is {name}, my age next year is {age + 1}, anniversary is {anniversary:%A, %B %d, %Y}.'
print(a)


value = 4 * 20 

print(f'The value is {value}.')


d = {0:10, 1:20}

for i in range(2):
    print(f'{i}:{d[i]}')


pprint.pprint("TEST ")