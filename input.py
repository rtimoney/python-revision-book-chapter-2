# create a variable to store the user input
name = input('Please enter your name: ')
print ('Hi' , name)
print ('Welcome to Coding for Beginners in easy steps')

# using commas automatically adds a space between items 
print ('Remember to have fun' , name , '!')

# use a + to concantenate without adding spaces
print ('Remember to have fun' , name + '!')

# data types
# str = string
# int = integer, whole number
# float = number with decimal point
# bool = boolean, true / false
# use type() to see what kind of data is currently stored in a variable 


town = 'Sligo'
print(town , 'is' , type(town))
kilo = 1000
print(kilo , 'is' , type(kilo))
temp = 13.50
print(temp , 'is' , type(temp))
flag = True
print(flag , 'is' , type(flag))

# int(x) converts x to an integer
# float(x)
# str(x)

num1 = input('enter a whole number:')
num2 = input('enter another whole number:')
# the inputs will be automatically stored as strings

print('The numbers are' , type(num1) , type(num2))

total = num1 + num2
print('Total:', total, type(total))

total = int(num1) + int(num2)
print('Total:', total, type(total))

total = float(num1) + float(num2)
print('Total:', total, type(total))
