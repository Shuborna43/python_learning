import login

def main():
    while True:
        first_name = input("please enter your first name:  ")
        last_name = input("please enter your last name:  ")
        student_ID = input("please enter your student ID:  ")
        default_password = login.generate_password(first_name, last_name, student_ID)
        if len(default_password) < 7:
            print (f"{default_password} is too short, atleast add 7 characters") 
        else:
            break 
 
    new_password = login.change_password()
    print(f"Your new password is: {new_password}") 

if __name__ == "__main__":
    main()
