#**python Exercise-Solutions - Chapter 3**
# 3-1: Names
# Store the names of a few of your friends in a list called names.Print
# each person's name by accessing each element in the list, one at a time.
names = ['Zulfi', 'Mohsin', 'Shad']

print(names[0])
print(names[1])
print(names[2])
#====================================
# 3-2: Greetings
# Start with the list you used in Exercise 3-1, but instead of just printing
# each person's name, print a message to them. The text of each message should
# be the same, but each message should be personalizedwith the person's name.
ames = ['zulfi', 'mohsin', 'shad']

msg = f"Hello, {names[0].title()}!"
print(msg)

msg = f"Hello, {names[1].title()}!"
print(msg)

msg = f"Hello, {names[2].title()}!"
print(msg)
#===============================================
# 3.3 your own list
# Think of your favorit mode of transportation , such as a motorcycle, or a car, and
# make a list that stores several examples.Use your list to print series of 
# statements about these items. such as "I would like to own a Honda motorcycle."

modes_of_transportation = ["motorcycle", "car", "bicycle", "scooter", "bus", "train"]
# Statements about Each Mode of Transportation
for mode in modes_of_transportation:
    if mode == "motorcycle":
        print(f"I would like to own a Honda {mode}.")
    elif mode == "car":
        print(f"A Tesla {mode} would be my dream car.")
    elif mode == "bicycle":
        print(f"I enjoy riding my {mode} around the neighborhood.")
    elif mode == "scooter":
        print(f"A Vespa {mode} is perfect for city commuting.")
    elif mode == "bus":
        print(f"The double-decker {mode} is a great way to explore the city.")
    elif mode == "train":
        print(f"I love taking the {mode} for long journeys.")

#=====================================================================
# 3-4: Guest List
# If you could invite anyone, living or deceased, to dinner, who would you invite?
# Make a list that includes at least three people you'd like to invite to dinner.
# Then use your list to print a message to each person, inviting them to dinner.
guests = ['Zulfiqar', 'Mohsin', 'Shamshad']

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")
#===========================================
# 3-5: Changing Guest List
# You just heard that one of your guests can't make the dinner, so you need to
# send out a new set of invitations. You'll have to think of someone else to invite.
# Start with your program from Exercise 3-4. Add a print() call at the end of your 
# program, stating the name of the guest who can't make it.Modify your list, replacing
# the name of the guest who can't make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.
# Invite some people to dinner.
guests = ['Zulfiqar', 'Mohsin', 'Shamshad']

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

# Mohsin can't make it! Let's invite Jalil instead.
del(guests[1])
guests.insert(1, 'Abdul Jalil')

# Print the invitations again.
name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")
#============================================
# 3-6: More Guests
# You just found a bigger dinner table, so now more space is available. 
# Think of three more guests to invite to dinner.
# Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# call to the end of your program, informing people that you found a bigger
# dinner table.Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.Use append()
# to add one new guest to the end of your list. Print a new set of invitation
# messages, one for each person in your list.
# Invite some people to dinner.
guests = ['Zulfiqar', 'Abdul Jalil', 'Shamshad']

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

# Jalil can't make it! Let's invite Mohsin instead.
del(guests[1])
guests.insert(1, 'Mohsin')

# Print the invitations again.
name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

# We got a bigger table, so let's add some more people to the list.
print("\nWe got a bigger table!")
guests.insert(0, 'Waqas')
guests.insert(2, 'Tayyeb')
guests.append('Afzal')

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[3].title()
print(f"{name}, please come to dinner.")

name = guests[4].title()
print(f"{name}, please come to dinner.")

name = guests[5].title()
print(f"{name}, please come to dinner.")
#=========================================
# 3-7: Shrinking Guest List
# You just found out that your new dinner table won't arrive in time for the 
# dinner, and you have space for only two guests.
# . Start with your program from Exercise 3-6. Add a new line that prints a 
#   message saying that you can invite only two people for dinner.
# . Use pop() to remove guests from your list one at a time until only two names
#   remain in your list. Each time you pop a name from your list, print a message
#   to that person letting them know you're sorry you can't invite them to dinner.
# . Print a message to each of the two people still on your list, letting them know
#   they're still invited.
# . Use del to remove the last two names from your list, so you have an empty list. Print
#   your list to make sure you actually have an empty list at the end of your program.
# Invite some people to dinner.
guests = ['ZXulfiqar', 'Mohsin', 'Shamshad']

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

# Mohsin can't make it! Let's invite Jalil instead.
del(guests[1])
guests.insert(1, 'Abdul Jalil')

# Print the invitations again.
name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

# We got a bigger table, so let's add some more people to the list.
print("\nWe got a bigger table!")
guests.insert(0, 'waqas')
guests.insert(2, 'Tayyeb')
guests.append('Afzal')

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[3].title()
print(f"{name}, please come to dinner.")

name = guests[4].title()
print(f"{name}, please come to dinner.")

name = guests[5].title()
print(f"{name}, please come to dinner.")

# Oh no, the table won't arrive on time!
print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

# There should be two people left. Let's invite them.
name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

# Empty out the list.
del(guests[0])
del(guests[0])

# Prove the list is empty.
print(guests)
#===========================================
# 3-8: Seeing the World
# . Think of at least five places in the world you'd like to visit.
# . Store the locations in a list. Make sure the list is not in alphabetical order.
# . Print your list in its original order. Don't worry about printing the list neatly,
#   just print it as a raw Python list.
# . Use sorted() to print your list in alphabetical order without modifying the actual list.
# . Show that your list is still in its original order by printing it.
# . Use sorted() to print your list in reverse alphabetical order without changing the 
#   order of the original list.
# . Show that your list is still in its original order by printing it again.
# . Use reverse() to change the order of your list. Print the list to show that its
#   order has changed.
# . Use reverse() to change the order of your list again. Print the list to show it's 
#   back to its original order.
# . Use sort() to change your list so it's stored in alphabetical order. Print the 
#   list to show that its order has been changed.
# . Use sort() to change your list so it's stored in reverse alphabetical order. 
#   Print the list to show that its order has changed.

locations = ['KSA', 'Behreen', 'Dubai', 'Masqad Uman', 'Iran']

print("Original order:")
print(locations)

print("\nAlphabetical:")
print(sorted(locations))

print("\nOriginal order:")
print(locations)

print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))

print("\nOriginal order:")
print(locations)

print("\nReversed:")
locations.reverse()
print(locations)

print("\nOriginal order:")
locations.reverse()
print(locations)

print("\nAlphabetical")
locations.sort()
print(locations)

print("\nReverse alphabetical")
locations.sort(reverse=True)
print(locations)
#================= END OF EXERCISE CHSPTER 3=======
