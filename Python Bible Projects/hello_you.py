# Ask user for name
name = input("Hello! What's your name?\n")
# Ask user for age
age = input("What's your age?\n")
# Ask user for city
city = input("What city are you located in?\n")
# Ask user for their favorite hobby
hobby = input("What's your favorite hobby?\n")
# Create output test
output = "Now, I know that your name is {}, you are {}, you live in {}, and you like {}!"
output = output.format(name,age,city,hobby)
# Print output
print(output)