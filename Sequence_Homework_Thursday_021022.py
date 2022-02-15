# Medium Question 6. Multiplication Table

# number = int(input("Enter the number you would like to print the multiplication table of: "))    
# for v in range(1,11):
#     print(number,'*',v,'=',v*number) <- this will print one multiplication table at a time


# # to print out a multiplication table:
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i} * {j} = {i*j}")





# Small

# 1. Sum the Numbers
# Create a list of numbers, print their sum.

# num = [1, 2, 3, 4, 9, 5]
# print(sum(num))

# another way to do this, the longer way, is using a for loop:

# num = [1, 2, 3, 4, 5]
# sum = 0
# for x in num:
#     sum+=x
# print(sum)






# 2. Largest Number
# Create a list of numbers, print the largest of the numbers.

# num = [1, 8, 456, 4, 5, 6]

# print("The largest number in this list is: ",max(num))

# The way it needs to be done using a for loop is below:

# using for loop

# nums = [2, 3, 5, 7, 11, 13, 17]

# max = 0

# for x in nums:
#     if(max < x):
#         max = x

# print(max)








# 3. Smallest Number
# Create a list of numbers, print the smallest of the numbers.

# num = [1, 8, 456, 4, 5, 6]
# print("The smallest number in this list it: ", min(num))


# nums = [2, 3, 5, 7, 11, 13, 1, 17]

# min = nums[0]

# for x in nums:
#     if (min > x):
#         min = x

# print(min)







# 4. Even Numbers
# Create a list of numbers, print each number in the list that is even.

# num = [1, 8, 456, 4, 5, 6, 99, 4309, 8490, 4830]

# for index in num:
#     if index % 2 == 0:
#         print(index)










# 5. Positive Numbers
# Create a list of numbers, print each number in the list that is greater than zero.

# num = [-5, 0, 1, 8, 456, 4, 5, 6]
# result = [v for v in num if v > 0]

# print(result)










# 6. Positive Numbers II
# Create a list of numbers, create a new list which contains every number in the given list which is positive.

# num = [-15, 1, 5, 9, 8, -78, 86, -4, -1, 0]
# posnum = [v for v in num if v > 0]

# print(posnum)










# 7. Multiply a list
# Create a list of numbers, and a single factor (also a number), create a new list consisting of each of the numbers in the first list multiplied by the factor. Print this list.

# num = [1, 2, 3, 4, 5]
# result = [v * 3 for v in num]

# print(result)









# 8. Reverse a String
# Given a string, print the string reversed.

# txt = "This is the final small problem for the sequence homework " [::-1]
# print(txt)

# txt = "This is the final small problem for the sequence homework "
# reverse = ""
# for char in txt:
#     reverse = char + reverse
# print(reverse)




# Medium Question 1. Multiply Vectors



# a_vector = [2, 4, 5] 
# b_vector = [2, 3, 6]
# c_vector = []

# for i in range(0, len(b_vector)):
#     c_vector.append(a_vector[i] * b_vector[i])
# print(c_vector)




# Medium Question 2: Matrix Addition

# a = [2, -2]
# b = [5, 3]
# c = []

# for i in range(0, len(b)):
#     c.append(a[i] + b[i])
# print(c)
# 
# 
# Above is the basic addition of two matrices, below is how you would configur addition using a nested loop with multiple matrices 


# a = [[1, 2], [3, 4]]
# b = [[5, 6], [7, 8]]
# c = []
# for i in range(0, 2):
#     for x in range(0, 2):
#         c.append(a[i][x] + b[i][x])
# print(c)


# Medium Question 3: Matrix Addition II


# a = [[1, 2, 3], [9, 10, 11], [16, 17, 18]]
# b = [[5, 6, 7], [13, 14, 15], [19, 20, 21]]
# c = []
# for i in range(0, len(a)):
#     for x in range(0, len(b)):
#         c.append(a[i][x] + b[i][x])
        
# print(c)















