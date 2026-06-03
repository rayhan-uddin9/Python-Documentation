# Class 07 - While Loops

# Basic while loop
count = 1
while count <= 5:
    print(count)
    count += 1      # same as count = count + 1

# while loop with break
number = 1
while True:
    print(number)
    number += 1
    if number > 5:
        break       # stops the loop

# while loop with continue
for i in range(1, 11):
    if i % 2 == 0:
        continue    # skip even numbers
    print(i)        # prints only odd numbers

# practical example - simple login
password = "python123"
while True:
    user_input = input("Enter password: ")
    if user_input == password:
        print("Access granted!")
        break
    else:
        print("Wrong password. Try again.")
