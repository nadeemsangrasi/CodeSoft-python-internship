import inquirer
import json
import random
from typing import Union

class MyContact():
    def load_data():
        try:
            with open("contact_info.txt","r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    contact_info:list[dict[str,Union[str,int]]] = load_data()
    def add_data(self,contact_info:list[dict[str,Union[str,int]]])->None:
        with open("contact_info.txt","w") as file:
            json.dump(contact_info,file)
    def add_contact(self,contact_info:list[dict[str,Union[str,int]]])->None:
        random_id =random.randint(1111,2222) 
        get_contact_info = inquirer.prompt([inquirer.Text("name",message="Enter contact name"),inquirer.Text("phone_number",message="Enter contact phone number"),inquirer.Text("email",message="Enter contact email"),inquirer.Text("address",message="Enter contact address")])
        if(get_contact_info["phone_number"].isdigit()):
            data = {"contact_id":random_id,"name":get_contact_info["name"],"phone_number":int(get_contact_info["phone_number"]),"email":get_contact_info["email"],"address":get_contact_info["address"]}
            contact_info.append(data)
            self.add_data(contact_info)
        else:
            print("Please enter valid phone number")
            
        self.main()
    def view_contact(self,contact_info:list[dict[str,Union[str,int]]]):
        if len(contact_info)!=0:
            print("your contact list")
            for i in range(len(contact_info)):
                print("#"*70)
                for key in contact_info[i]:
                    print(f"{key}:{contact_info[i][key]}")
            print("#"*70)
        else:
            print("add contact info first")
        self.main()
    def search_contact(self,contact_info:list[dict[str,Union[str,int]]]):
        if len(contact_info)!=0:
            contact_id=inquirer.prompt([inquirer.Text("id",message="Enter contact id")])
            isId=False
            if contact_id["id"].isdigit():
                for i in range(len(contact_info)):
                    if int(contact_id["id"])==contact_info[i]["contact_id"]:
                        isId=True
                        for key in contact_info[i]:
                            print(f"{key}:{contact_info[i][key]}")
                if not isId:
                    print("this id didn't exist")                  
                                  
            else:
                print("enter valid id")
        else:
            print("add contact info first")
        self.main()
    def update_contact(self,contact_info:list[dict[str,Union[str,int]]]):
        if len(contact_info)!=0:
            contact_id=inquirer.prompt([inquirer.Text("id",message="Enter contact id")])
            isId=False
            if contact_id["id"].isdigit():
                for i in range(len(contact_info)):
                    if int(contact_id["id"])==contact_info[i]["contact_id"]:
                        isId=True
                        get_new_contact_info = inquirer.prompt([inquirer.Text("name",message="Enter new contact name"),inquirer.Text("phone_number",message="Enter new contact phone number"),inquirer.Text("email",message="Enter new contact email"),inquirer.Text("address",message="Enter new contact address")])
                        contact_info[i]["name"]=get_new_contact_info["name"]
                        contact_info[i]["phone_number"]=int(get_new_contact_info["phone_number"])
                        contact_info[i]["email"]=get_new_contact_info["email"]
                        contact_info[i]["address"]=get_new_contact_info["address"]
                if not isId:
                    print("this id didn't exist")                  
                else:
                    print("contact updated successfully") 
            else:
                print("enter valid id")
        else:
            print("add contact info first")
        self.main()
    def delete_contact(self,contact_info:list[dict[str,Union[str,int]]]):
        if len(contact_info)!=0:
            contact_id=inquirer.prompt([inquirer.Text("id",message="Enter contact id")])
            isId=False
            if contact_id["id"].isdigit():
                for i in range(len(contact_info)):
                    if int(contact_id["id"])==contact_info[i]["contact_id"]:
                        isId=True
                        contact_info.pop(i)
                        break
                if not isId:
                    print("this id didn't exist")                  
                else:
                    print("contact deleted successfully") 

            else:
                print("enter valid id")
        else:
            print("add contact info first")
        self.main()
    def main(self):
        flage = True
        options :str=inquirer.prompt([inquirer.List("option",message="Select your desired option",choices=["Add Contact","View Contact List","Search Contact","Update Contact","Delete Contact","Exit"])])
        while flage:
            match options["option"]:
                case "Add Contact":
                    self.add_contact(self.contact_info)
                    break
                case "View Contact List":
                    self.view_contact(self.contact_info)
                    break
                case "Search Contact":
                    self.search_contact(self.contact_info)
                    break
                case "Update Contact":
                    self.update_contact(self.contact_info)
                    break
                case "Delete Contact":
                    self.delete_contact(self.contact_info)
                    break
                case "Exit":
                    flage=False
                    break

if __name__ =="__main__":
    contact :MyContact=MyContact()
    contact.main()            