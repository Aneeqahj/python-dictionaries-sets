# Exercise 1
# Task 1

b = input("Enter String:")
a = input("Enter Character:")
c = 0
for i in range(len(b)):
    if a == b[i]:
        c = c + 1
print(c)

# Task 2

num_to_word = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}
a = str(int(input("Enter number: ")))
num_list = list(a)
num_word = ""
for i in num_list:
    num_word = num_word + num_to_word[i] + " "
print(num_word)

# Task 3

colors = {'green', 'yellow', 'red', 'black', 'blue'}
c = int(input(" =How many colors would you like to add? "))
for i in range(c):
    q = input("What color would you like to add? ")
    colors.add(q)

for n in colors:
    print(n)
