# INDIVIDUAL ACTIVITY 2

'''

Once familiar with these components, we must prepare ourselves to carry out the following actions, to simulate the purchase through a web page

Based on the context: Think of a web application that seeks to solve a problem.
This application must provide the possibility to log in with an individual profile.
Generally, you enter your personal account on a page, and it greets you and recognizes you.
Let's try to replicate this.
● Create a string with the name of at least 7 users of your application.
● Now think of three of them. Look for them in the list with the appropriate method.
● What problems can arise if another person wants to search for a user and manually enters your name? How would you solve this problem?
● Convert your string to a list, in which each element is a user.
● Print on the screen the number of users your application has.
● Print a greeting message to the different users on the screen. What technique can you use to do this?


'''

# Create a string with the name of at least 7 users of your application.
user = 'user1 user2 user3 user4 user5 user6 user7'

# Now think of three of them. Look for them in the list with the appropriate method.
searchedUser = input("Insert username: ")

if searchedUser in user:
    print(f'Hello {searchedUser}')
else:
    print('User Not Found')
    
# What problems can arise if another person wants to search for a user and manually enters your name? How would you solve this problem?
'''
That you enter one of the characters in uppercase or lowercase and in the database it is in a different format than the one searched for.
It can be worked around by implementing a method to make the fetched data fully uppercase, lowercase, or uppercase, as required.
'''

# Convert your string to a list, in which each element is a user.
userList = user.split(" ")
print(f'The number of users is: {len(userList)}')

# Print a greeting message to the different users on the screen. What technique can you use to do this?
for usu in userList:
    print(f'Greetings {usu}!') 
