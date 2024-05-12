import inquirer
import random
def normal_password():
    length_of_password=inquirer.prompt([inquirer.Text("length",message="Enter password length")])
    password=""
    if length_of_password["length"] and length_of_password["length"].isdigit():
        password_character = "abcdefghijklmnopqrstuvwxyz"
        for i in range(int(length_of_password["length"])):
            random_index= random.randint(1,len(password_character)-1)
            password+=password_character[random_index]
        print("*"*30)
        print(f"password generated successfully\nyour password is '{password}'")
        print("*"*30)
        generate_again = inquirer.prompt([inquirer.Confirm('generate_again', message="Do you want to generate again?")])
        if generate_again["generate_again"]:
            normal_password()
    else:
        print("Please enter correct length")
    main()
def moderate_password():
    length_of_password=inquirer.prompt([inquirer.Text("length",message="Enter password length")])
    password=""
    if length_of_password["length"] and length_of_password["length"].isdigit():
        password_character = "abcdefghijklmnopqrstuvwxyz1234567890"
        for i in range(int(length_of_password["length"])):
            random_index= random.randint(1,len(password_character)-1)
            password+=password_character[random_index]
        print("*"*30)
        print(f"password generated successfully\nyour password is '{password}' ")
        print("*"*30)
        generate_again = inquirer.prompt([inquirer.Confirm('generate_again', message="Do you want to generate again?")])
        if generate_again["generate_again"]:
            moderate_password()
    else:
        print("Please enter correct length")
    main()
def strong_password():
    print("strong password should have minimum 8 characters")
    length_of_password=inquirer.prompt([inquirer.Text("length",message="Enter password length")])
    password=""
    if length_of_password["length"] and length_of_password["length"].isdigit():
        if int(length_of_password["length"])>=8:
            password_character = "abcdefghijklmnopqrstuvwxyz12345678910ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"
            for i in range(int(length_of_password["length"])):
                random_index= random.randint(1,len(password_character)-1)
                password+=password_character[random_index]
            print("*"*30)
            print(f"password generated successfully\nyour password is '{password}' ")
            print("*"*30)
            generate_again = inquirer.prompt([inquirer.Confirm('generate_again', message="Do you want to generate again?")])
            if generate_again["generate_again"]:
                strong_password()
        else:
            print("strong password length must be 8 or above")
    else:
        print("Please enter correct length")
    main()
def main():
    print("*"*30)
    print("Passoword Generator")
    print("*"*30)
    flage=True
    while flage:
        password_type=inquirer.prompt([inquirer.List("type",message="select password type",choices=["Normal","Moderate","Strong","Quit"])])
        match password_type["type"]:
            case "Normal":
                normal_password()
                break
            case "Moderate":
                moderate_password()
                break
            case "Strong":
                strong_password()
                break
            case "Quit":
                print("Good bye have a nice day")
                flage=False
                break
if __name__ =="__main__":
    main()