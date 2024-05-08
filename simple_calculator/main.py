import inquirer
print("Simple Calculator")
numbers :int= inquirer.prompt([inquirer.Text("firstNumber",message="Enter first number"),inquirer.Text("secondNumber",message="Enter second number")])
operations :list[str]=inquirer.prompt([inquirer.List("operations",message="Select operations",choices=["Addition","Subtraction","Multiplication","Division","Modulus","Quit"])])
match operations["operations"]:
    case "Addition":
        print(int(numbers["firstNumber"])+int(numbers["secondNumber"]))
    case "Subtraction":
        print(int(numbers["firstNumber"])-int(numbers["secondNumber"]))
    case "Multiplication":
        print(int(numbers["firstNumber"])*int(numbers["secondNumber"]))
    case "Division":
        print(int(numbers["firstNumber"])/int(numbers["secondNumber"]))
    case "Modulus":
        print(int(numbers["firstNumber"])%int(numbers["secondNumber"]))
    case "Quit":
        print("bye bye Have a nice day")
    

        


