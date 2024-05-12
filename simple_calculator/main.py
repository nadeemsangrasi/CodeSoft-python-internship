import inquirer
print("Simple Calculator")
def calculate():
    numbers :int= inquirer.prompt([inquirer.Text("firstNumber",message="Enter first number"),inquirer.Text("secondNumber",message="Enter second number")])
    operations :list[str]=inquirer.prompt([inquirer.List("operations",message="Select operations",choices=["Addition","Subtraction","Multiplication","Division","Modulus","Quit"])])
    if not len(numbers["firstNumber"])==0 and not len(numbers["secondNumber"])==0 and numbers["firstNumber"].isdigit() and numbers["secondNumber"].isdigit():
        match operations["operations"]:
            case "Addition":
                print("Addition = {}".format(int(numbers["firstNumber"])+int(numbers["secondNumber"])))
            case "Subtraction":
                print("Subtraction = {}".format(int(numbers["firstNumber"])-int(numbers["secondNumber"])))
            case "Multiplication":
                print("Multiplication = {}".format(int(numbers["firstNumber"])*int(numbers["secondNumber"])))
            case "Division":
                print("Division = {}".format(int(numbers["firstNumber"])/int(numbers["secondNumber"])))
            case "Modulus":
                print("Modulus = {}".format(int(numbers["firstNumber"])%int(numbers["secondNumber"])))
            case "Quit":
                print("bye bye Have a nice day")
    else:
        print("Enter valid numbers")
    calculate_again = inquirer.prompt([inquirer.Confirm('calculate_again', message="Do you want to calculate again?")])
    if calculate_again["calculate_again"]:
        calculate()
    
calculate()
        


