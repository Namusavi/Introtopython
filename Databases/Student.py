from database import Student

try:
    jina = input("Enter Name\n")
    nambariyasimu = input("Enter phone number\n")
    miaka = input("Enter age\n")
    jinsia = input("Enter gender\n")
    nambari = input("Enter phone student code\n")

    Student.create(name=jina, phonenumber=nambariyasimu, age=miaka, gender=jinsia, studentcode=nambari)
    print("Student Created Successfully")

except:
    print("Failed to Create User")
