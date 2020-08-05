# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# for i in range(1, 7):
#   for j in range(1, i):
#     print(j, end = "")
#   print()
# for i in range(5):
#   print(i)

# for b in range(5):
#   for c in range(4):
#     print("hello")


# Write a Python program to test if a number is positive or negative. The program will ask the user to input a number, then it will
# display what the number is.

num = input("Enter a number: ")
num = float(num)

# conditional to assess whether num is positive, negative or zero.

if (num < 0):
  print("negative ")
elif (num == 0):
  print("that's zero")
else:
  print("positive")