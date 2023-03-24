"""
Write a python script that take input from a user and display it to the
 user in a well formatted output.(use the concept of lists)
 Details:
 Name,Age,Class,Gender,Telephone
"""

userDetails = []
userInput = input("Enter a name: ")
userDetails.append(userInput)
userInput = input("Enter age: ")
userDetails.append(userInput)
userInput = input("Enter your class: ")
userDetails.append(userInput)
userInput = input("Enter gender: ")
userDetails.append(userInput)
userInput = input("Enter your telephone number: ")
userDetails.append(userInput)

print(f"My name is {userDetails[0]} " )
print(f"I am  {userDetails[1]} years old " )
print(f"I am in  {userDetails[2]} " )
print(f"I am a {userDetails[3]} " )
print(f"This is my telephone number {userDetails[4]} " )
print(userDetails)