#**Exercises - Solutions - Chapter 2**
# 2.1 (Simple Message)
# Assign a message to a variable, and then print that message.
msg = "I love learning to use Python,which is so intrested."
print(msg)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++
# 2-2: Simple Messages
# Assign a message to a variable, and print that message. 
# Then change the value of the variable to a new message, and print the new message.

msg = "I love learning to use Python."
print(msg)

msg = "It's really very easy and satisfying!"
print(msg)
#++++++++++++++++++++++++++++++++++++++++++++
# 2-3: Personal Message
# Use a variable to represent a person’s name, and print a message to that person.
# Your message should be simple, such as, “Hello Eric, would you like to learn some 
# Python today?”
name = "zulfiqar"
msg = f"Hi {name.title()}, would you like to learn modern Python type static today?"
print(msg)
#+++++++++++++++++++++++++++++++++++++++++++++++
# 2-4: Name Cases
# Use a variable to represent a person’s name, and then print that
# person’sname in lowercase, uppercase, and title case.
name = "zulfiqar"
print(name.lower())
print(name.upper())
print(name.title())
#++++++++++++++++++++++++++++++++++++++++++++++++++
# 2-5: Famous Quote
# Find a quote from a famous person you admire. Print the quote and the name of its author.
# Your output should look something like the following, including the quotation marks:
# Albert Einstein once said,
# "A person who never made a mistake never tried anything new."

print('Albert Einstein once said, "A person who never made a mistake')
print('never tried anything new."')
#++++++++++++++++++++++++++++++++++++++++++++++++++++
# 2-6: Famous Quote 2
# Repeat Exercise 2-5, but this time, represent the famous person’s 
# name using a variable called famous_person. Then compose your message
# and represent it with a new variable called message. Print your message.
famous_person = "Albert Einstein"
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'
print(message)
#it can also be write as
famous_person = "Albert Einstein"

message = f'{famous_person} once said, "A person who never made a mistake'
message += ' never tried anything new."'

print(message)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 2-7: Stripping Names
# Use a variable to represent a person's name, and include some whitespace characters at
# the beginning and end of the name. Make sure you use each character combination,
# "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed. Then print the name
# using each of the three stripping functions, lstrip(), rstrip(), and strip().

name = "\tZulfiqar Mughal\n"
print("Unmodified:")
print(name)
print("\nUsing lstrip():")
print(name.lstrip())
print("\nUsing rstrip():")
print(name.rstrip())
print("\nUsing strip():")
print(name.strip())
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 2-8: File Extensions
# Python has a removesuffix() method that works exactly like removeprefix().
# Assign the value 'python_notes.txt' to a variable called filename.
# Then use the removesuffix() method to display the filename without the
# file extension, like some file browsers do.
filename = 'python_notes.txt'
simple_filename = filename.removesuffix('.txt')

print(simple_filename)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#2-9 Number Eight
# Write addition, subtraction, multiplication and division operaions 
# that each result in the number 8. Be sure to enclose your oprations
# in print() calls to see the result.You should creat four lines that
# look likes this : print (5+3).
# your out puts shpuld be four lines, with the number 8 oppearing once
# on each line
# 
print(5+3)
print(10-2)
print(4*2)
print(16/2)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 2-10: Favorite Number
# Use a variable to represent your favorite number. Then, using that variable,
# create a message that reveals your favorite number. Print that message.

fav_num = 786
msg = f"My favorite number is {fav_num}."

print(msg)
#++++++++++++++++ END OF EXERCISE CHAPTER = 2

