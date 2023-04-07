# This programm says hello and ask for my name.
print('Hello friend')
print('What is your Name?') #Ask for your Name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age') #Ask for your Age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
# Making and 'INT' into a 'STR'
print('I am ' + str(90) + ' years old.')

print('Write an Integer')
spam = input()
spam = int(spam)
print(type(spam))
print('Your value + 1 is...' )
print(spam + 1)
