# # Small Question 1. Hello You!
# name = input('What is your name? ')
# greeting = f'Hello, {name}!'
# print(greeting)



# # Small Question 2. HELLO YOU!
# name = input('WHAT IS YOUR NAME? ')
# length = len(name)
# greeting = f'hello, {name}!\nyour name has {length} letters in it! Awesome!'
# print(greeting.upper())



# Small Question 3: MADLIB
# greeting = "Please fill in the blanks below:\n____(name)____'s favorite subject in school is ____(subject)____"
# print(greeting)
# name = input('What is the name you would like to use? ')
# subject = input('What is the subject you would like to use? ')
# final_greeting = f'{name}\'s favorite subject in school is {subject}.'
# print(final_greeting)


# # Small Question 4. Days of the Week
# day = int(input('Day (0-6)? '))

# print(day)

# if day==0:
#     print('Sunday')
# elif day==1:
#     print('Monday')
# elif day==2:
#     print('Tuesday')
# elif day==3:
#     print('Wednesday')
# elif day==4:
#     print('Thursday')
# elif day==5:
#     print('Friday')
# elif day==6:
#     print('Saturday')
# else:
#     print("Please enter a valid number")



# # Small Question 5. Work or Sleep In?

# day = int(input('Day (0-6)? '))

# print(day)

# if day==0:
#     print('Sleep in')
# elif day==1:
#     print('Go to work')
# elif day==2:
#     print('Go to work')
# elif day==3:
#     print('Go to work')
# elif day==4:
#     print('Go to work')
# elif day==5:
#     print('Go to work')
# elif day==6:
#     print('Sleep in')
# else:
#     print("Entry invalid, please try again")



# Small Question 6. Celsius to Fahrenheit

# C = int(input("Enter temperature in Celsius "))
# F = (C * 9/5) + 32;
# print(F)



# Small Question 7. Looping from 1 to 10

# a = 0
# while a < 10:
#   a += 1  
#   print(a)
    



# Small Question 8. n to m
# MIN = int(input('What number would you like to start the sequence? '))

# MAX = int(input('What number would you like to end the sequence? '))

# start = MIN 
# stop = MAX

# while MIN <= MAX:
#     print(MIN)
#     MIN += 1


# Small Question 9. Print a Square


# height = 5
# for i in range(height,0,-1):
#     print('*' * 5)


# Small Question 10








# Medium Question 1. Tip Calculator

# 1. Tip Calculator

# bill = float(input('Total bill amount? $'))
# print("$%.2f" % bill)

# service = input("""
#                 Level of service? 
                
#                 Good
#                 Fair
#                 Bad
                
#                 """)

# # total = bill + (bill * service)

# if service.lower() == 'good':
#     tip = (bill * 0.2)
#     total = bill + tip
#     print("Tip amount: $%.2f" % tip)
#     print("Total amount: $%.2f" % total)
# elif service.lower() == 'fair':
#     tip = (bill * 0.15)
#     total = bill + tip
#     print("Tip amount: $%.2f" % tip)
#     print("Total amount: $%.2f" % total)
# elif service.lower() == 'bad':
#     tip = (bill * 0.1)
#     total = bill + tip
#     print("Tip amount: $%.2f" % tip)
#     print("Total amount: $%.2f" % total)
# else:
#     print('Please enter a valid service level ')






# Medium Question 6. Multiplication Table

# number = int(input("Enter the number you would like to print the multiplication table of: "))    
# for v in range(1,11):
#     print(number,'*',v,'=',v*number)












