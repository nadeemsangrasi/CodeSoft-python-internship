import inquirer
import json 

def main()->None:
    def load_data():
        try:
            with open("./myTodos.txt","r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    def write_todos(todos:str):
        with open("./myTodos.txt","w") as file:
            json.dump(todos,file)
    def add_todo(todos):
        todo = inquirer.prompt([inquirer.Text("todo",message="write you todo")])
        todos.append(todo["todo"])
        write_todos(todos)
        print("Todo added successfully\n'{}'".format(todo["todo"]))
        add_more_todo = inquirer.prompt([inquirer.Confirm('addMore', message="Do you want to add more todos?")])
        if add_more_todo["addMore"]:
            add_todo(todos)

    def check_todos(todos:list[str]):
        print("Your todos")
        for i in range(len(todos)):
            print(f"{i+1}) {todos[i]}")
    def update_todos(todos:list[str]):
        index_to_update = inquirer.prompt([inquirer.Text("index",message="Enter index number to delete todo")])
        updated_todo = inquirer.prompt([inquirer.Text("updatedTodo",message="write new todo")])
        todos[int(index_to_update["index"])-1]=updated_todo["updatedTodo"]
        print(f"Todo updated successfully")
    def delete_todos(todos:list[str]):
        index_to_delete = inquirer.prompt([inquirer.Text("index",message="Enter index number to delete todo")])
        deleted_todo = todos.pop(int(index_to_delete["index"])-1)
        print("Todo deleted successfully\n'{}'".format(deleted_todo))

    flage:bool=True
    todos:list[str] = load_data() 
    while flage:
        print("*"*70)
        print("Welcome to my Todo App")
        print("*"*70)
        choice = inquirer.prompt([inquirer.List("choice",message="Choose your desired option",choices=["1) Add todo","2) Check todos","3) Update todos","4) Delete todos","5) Quit app"])])
        match choice['choice']:
            case "1) Add todo":
                add_todo(todos)  
            case "2) Check todos":
                check_todos(todos)
            case "3) Update todos":
                update_todos(todos)
            case "4) Delete todos":
                delete_todos(todos)
            case "5) Quit app":
                flage:bool=False
                break

if __name__ =="__main__":
    main()