import pathfinder as p
import json

class bank:
    def __init__(self) -> None:
        self.user = "none"
        self.userdict = "null"
        self.update_ac_data()

    def update_ac_data(self):
        accountsf = open(p.path("data/accounts.json"),'r')
        self.accounts = json.load(accountsf)
        accountsf.close()
        if self.user != "none":
            self.userdict = dict(self.accounts[self.user])

    def transact(self,money):
        accountsf = open(p.path("data/accounts.json"),'w')
        self.userdict["money"] += money
        self.accounts[self.user] = self.userdict
        json.dump(self.accounts,accountsf)
        accountsf.close()

    def show_help(self):
        help = open(p.path("assets/help.txt"),'r')
        print(help.read())
        help.close()

    def login(self,id):
        if self.user == "null":
            print("someone already logged in, please logout before loggin in")
            return
        if id not in self.accounts:
            print("account not found, please enter a valid account")
            return
        self.user = id
        self.update_ac_data()
        print("Logged in as",id)

    def logout(self):
        if self.user == "none":
            print("no one is logged in")
            return
        self.user = "none"
        self.userdict = "null"
        print("logged out")

    def register(self,id,password):
        if id != "null":
            print("some one is logged in, please logout before making a account")
        if id in self.accounts:
            print("account name already used, try another")
            return
        if password == "null" or len(password)<8:
            print("invalid password, these are the requirment:\n    #password must be longer than 8 characters")
            return
        self.accounts[id] = {"password":password,"money":0}
        accountsf = open(p.path("data/accounts.json"),'w')
        json.dump(self.accounts,accountsf)
        accountsf.close()
        
        print("account created, please remember your password")

    def unregister(self,id,password):
        if id == "null" or password == "null":
            print("please enter name and password, check out 'help'")
            return
        accountsf = open(p.path("data/accounts.json"),'w')
        if id in self.accounts:
            if password == self.accounts[id["password"]]:
                self.accounts[id].pop()
                json.dump(self.accounts,accountsf)
            else:
                print("invalid password, try again")
        else:
            print("this account does not exists")
        accountsf.close()

    def info(self):
        print("all users:",self.accounts)
        print("logged in:",self.user)
        print("data:",self.userdict)

    def check_balance(self):
        if self.user == "none":
            print("you are not logged in, log in to check your balance")
            return
        print("you have",self.userdict["money"],"rupees balance remaining in your account currently")   

    def deposit(self,amt):
        if self.user == "none":
            print("no one is logged in, please log in to continue")
            return
        if amt <= 0:
            print("invalid amount")
        self.transact(amt)
        print("Deposited",amt,"to [{}] account".format(self.user))

    def withdraw(self,amt):
        if self.user == "none":
            print("no one is logged in, please log in to continue")
            return
        if self.userdict["money"] < amt:
            print("not enough balance, please enter amount within your balance.")
            return
        if amt<= 0:
            print("invalid amount")
        self.transact(-amt)
        print("withdrew",amt,"from [{}] account".format(self.user))

    def exit(self):
        print("Thank you for using.\nexiting...")
        accountsf = open(p.path("data/accounts"),'w')
        self.accounts[self.user] = self.userdict
        json.dump(self.accounts,accountsf)
        accountsf.close()
        exit()