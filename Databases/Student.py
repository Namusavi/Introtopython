from database import User

try:
    jina = input("Enter Name\n")
    nambarisimu = input("Enter phone number\n")
    miaka = input("Enter age\n")
    jinsia = input("Enter gender\n")
    nambari = input("Enter phone student code\n")
    User.create(name=jina, phonenumber=nambarisimu, miaka=age, gender=jinsia, studentcode=nambari)
    print("User Created Successfully")

except:
    print("Failed to Create User")
