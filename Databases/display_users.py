from database import User

users = User.select()
#use for loop to display
for user in users:
    print(user.name, user.email, user.password)

from database import User

users = User.select()
#use for loop to display
for user in users:
    print(user.name, user.phonenumber, user.age, user.gender, user.studentcode)