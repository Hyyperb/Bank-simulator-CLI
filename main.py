import Bank
import pathfinder as p
import os.path


bank = Bank.bank()

inp_style = ">>"

cmdlist = {
    "help":["help","manual","h"],
    "login":["login","signin","l"],
    "logout":["logout","signout","o"],
    "register":["register","signup","r"],
    "unregister":["unregister","delete","u"],
    "check balance":["check","balance","c"],
    "deposit":["deposit","add","d"],
    "withdraw":["withdraw","sub","w"],
    "exit":["exit","quit","x"],
    "info":["debug_info"]
}

with open(p.path("assets/welcome.txt")) as welcome_text:
    print(welcome_text.read())

def main():
    value_command = "null"
    second_value_command = "null"
    command = input(inp_style)
    command_split = command.split(' ')
    main_command = command_split[0]

    if len(command_split)>1:
        value_command = command_split[1]
    if len(command_split)>2:
        second_value_command = command_split[2]

    if main_command in cmdlist["help"]:
        bank.show_help()

    elif main_command in cmdlist["login"]:
        bank.login(value_command)

    elif main_command in cmdlist["logout"]:
        bank.logout()
        
    elif main_command in cmdlist["register"]:
        bank.register(value_command,second_value_command)

    elif main_command in cmdlist["unregister"]:
        bank.unregister(value_command,second_value_command)

    elif main_command in cmdlist["check balance"]:
        bank.check_balance()

    elif main_command in cmdlist["deposit"]:
        bank.deposit(int(value_command))

    elif main_command in cmdlist["withdraw"]:
        bank.withdraw(int(value_command))
    
    elif main_command in cmdlist["exit"]:
        bank.exit()

    elif main_command in cmdlist["info"]:
        bank.info()

    elif main_command == "":
        pass
    else:
        print("invalid command, type 'help' for help")
    

while True:
    main()