# Sum of Numbers in Python
# https://github.com/MikeTechSecurity/SumOfNumbers

# Initialize sum to 0
sum = 0

# Provide a prompt to the user
userInput = int(input("Enter a positive number or a negative number to stop: "))

# Continue the loop as long as the user enters non-negative numbers
while userInput >= 0:
    # Add the value of userInput to the current value of sum
    sum += userInput
    
    # Prompt the user again
    userInput = int(input("Enter another positive number or a negative number to stop: "))

# Display the final value of sum
print ("The total sum of the positive numbers is:", sum)