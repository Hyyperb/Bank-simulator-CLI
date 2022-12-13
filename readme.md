# Bank Simulator CLI

This is one of my old practice project.
All the code written is very messy
but i think i'll guide you enough to understand it

### Installation and usage
run this command to get it on your pc
```bash
git clone https://github.com/HyperBhavik28/Bank-simulator-CLI
```

go to the folder
```bash
cd Bank-simulator-CLI
```

run using python command
```
python main.py
```


### File structure

The **bank.py** file contains a `Bank` class which is accessed through a cli interface in the **main.py** file

The **data** folder is used to store a `accounts.json` folder which contains all the data of the bank like users, how much money they have and even their passwords without any protection *yet*

The **assets** folder contains .txt files with ascii art and other text files in them

`pathfinder.py` is a stupid name i gave to a file for a separate function that can be used to find the path of the the files something shit i forgot dw i'll fix this later

### Manual

help/manual/h: 
	Display this help page

login/signin/l:
	Login using your username
	>>login username

logout/signout/o:
	Logout the currently logged in user
	
register/signup/r:
	register a new user
	>>register username password

unregister/delete/u:
	Deletes an account
	>>unregister username password

check/balance/c:
	Check balance of logged in user

deposit/add/d:
	Deposit money in bank
	>>deposit amount

withdraw/sub/w:
	Withdraw money from bank
	>>withdraw amount

exit:
	Exits from this program

debug_info:
	Returns raw bank data

