import login

def main():
 first_name = input("please enter your first name:  ")
 last_name = input("please enter your last name:  ")
 student_ID = input("please enter your student ID:  ")
 default_password = login.generate_password(first_name, last_name, student_ID)
 print("Your default password is: ", default_password)

if __name__ == "__main__":
    main()