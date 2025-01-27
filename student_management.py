# Bussiness Layer

class Student:
  def __init__(self,name=None,age=None,address=None,grade=None,username=None,password=None):
    self.__student_db = {}
    self.__std_name = name
    self.__std_age = age
    self.__std_address = address
    self.__std_grade = grade
    self.__std_username = username
    self.__std_password = password

  def __show_detail(self,username):
    password = self.__student_db.get(username).get("std_password")
    name = self.__student_db.get(username).get("std_name")
    age = self.__student_db.get(username).get("std_age")
    class_ = self.__student_db.get(username).get("std_class")
    address = self.__student_db.get(username).get("std_address")
    print("*********Student Details**********")
    print(f" Name:{name}\n Age:{age}\n class:{class_}\n Address:{address}\n Username:{username}\n Password:{password}\n")
    print()  

  def __update_detail(self,username):
    student = {}
    student["std_name"] = input("Enter Student name:")
    student["std_password"] = input("Enter Student password:")
    student["std_age"] = int(input("Enter Student age:"))
    student["std_class"] = input("Enter Student class:")
    student["std_address"] = input("Enter Student address:")
    self.__student_db[username] = student
    print("Student updated successfully..")
    self.__show_detail(username)

  def __change_password(self,username):
    counter = 0
    while True:
      if counter == 3:
        break
      old_password = input("Enter Student old password:")
      new_password = input("Enter Student new password:")
      if self.__student_db.get(username).get("std_password") == old_password:
        self.__student_db.get(username)["std_password"] = new_password
        print("Student passowrd updated with new password.")
        break
      else:
        print("Incorrect Old password.")
        counter +=1  

  def __registeration(self):
    student = {}
    std_userid = input("Enter Student User Id:")
    student["std_name"] = input("Enter Student name:")
    student["std_password"] = input("Enter Student password:")
    student["std_age"] = int(input("Enter Student age:"))
    student["std_class"] = input("Enter Student class:")
    student["std_address"] = input("Enter Student address:")
    self.__student_db[std_userid] = student
    print("Student Added successfully..")
    print(self.__student_db)

  def __home(self,username):
    counter = 0
    while True:
      if counter == 3:
        break

      choice=input("""
    1 show details.
    2 update details. 
    3 change password. 
    4 logout.                          
    """)
      
      if choice == "1":
        self.__show_detail(username)
      elif choice == "2":
        self.__update_detail(username)
      elif choice == "3":
        self.__change_password(username)  
      elif choice == "4":
        break
      else:
        print("Invalide input Please Try again...") 
        counter +=1


  def __login(self):
    username = input("Enter Student User Id:")
    password = input("Enter Student password:")
    if self.__student_db.get(username) is not None:
      if self.__student_db.get(username).get("std_password") == password:
        self.__home(username)
      else:
        print("Incorrect password.")
    else:
      print("Incorrect username.")    


# Presentation Layer

  def mainlogic(self):
    print("************Welcome To Student Management System************")
    counter = 0
    while True:
      if counter == 3:
        break

      choice=input("""
    1 Registeration.
    2 Login. 
    3 Exit.             
    """)
      
      if choice == "1":
        self.__registeration()
      elif choice == "2":
        self.__login()
      elif choice == "3":
        break  
      else:
        print("Invalide input Please Try again...") 
        counter +=1

if __name__ == "__main__":
  std = Student()
  std.mainlogic()
