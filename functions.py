#!/bin/python3
'''
def add_two_num(num1, num2):
    return (num1+num2)

sum = add_two_num(4, 6)
print(sum)
'''

'''
def add(num1, num2):
    print(f'The sum of {num1} and {num2} is {num1+num2}')

add(12, 3)
'''

"""
def compare(n1, n2):
    if n1 > n2:
        print('The first number is greater')
    elif n1 < n2:
        print('The second number is greater')
    else:
        print('Both numbers are equal')
    return 'done!'

num1, num2, num3, num4, num5 = 4, 2, 5, 13, 3

compare(num1, num2)
compare(num3, num4)
r_val = compare(num5, num5)
print(r_val)
"""

'''
# Using loops and nexted loops

for i in range(1, 11):
    print(i, end=' ')
print()
'''

# In C, we'll have the above code as:
# for (int i = 1; i < 11; i++)
#        printf('%d ', i);
# putchar('\n');
"""
password = ""
while(True):
    if (password != 'matilda123'):
        password = input("Enter your password, please: ")
    else:
        print("Correct password!")
        break
"""

i = 1
print("Using while loop...")
while(i < 11):
    print(i)
    i = i+1 # i += 1 || i++

# print("Using do-while loop...")
