"""
   Joey Parshley
   MET CS 521 O2
   17 APR 2018
   hw_6_12_3
   Description: Use the Account class created in Exercise 7.3 to simulate an 
                ATM machine. Create ten accounts in a list with the ids 
                0 , 1 , ..., 9 , and an initial balance of $100. The system 
                prompts the user to enter an id. If the id is entered 
                incorrectly, ask the user to enter a correct id. Once an id is 
                accepted, the main menu is displayed as shown in the sample 
                run. You can enter a choice of 1 for viewing the current 
                balance, 2 for withdrawing money, 3 for depositing money, 
                and 4 for exiting the main menu. Once you exit, the system will 
                prompt for an id again. So, once the system starts, it 
                won’t stop.


"""
from account import Account
# Create list of Account objects
accounts = [ Account(id) for id in range(10)]

def checkBalance(account_id):
    """
    Description: Gets the balance of the for the account object associated with 
    the account_id
        :account_id : Int 
        :return : None : calls askForMenuOption(account_id)

    """
    # call the getBalance method on the accounts object for account_id
    print('The balance is {}'.format(accounts[account_id].getBalance()))
    # Ask the user to make a menu selection
    askForMenuOption(account_id)

def withdraw(account_id):
    """
    Description: lets user withdraw amount from account object associated with  
    the account_id
        :account_id : Int 
        :return : None : withdraws amount from account

    """
    invalidEntry = True
    msg = "{} is not a number no withdraw was made."
    # Ask user for the ammount to withdraw making sure that it is a number
    while invalidEntry:
        try:
            withdrawal_amount = input("Enter the amount to withdraw: ")
            withdrawal_amount = int(withdrawal_amount)
            invalidEntry = False
        except:
            print(msg.format(withdrawal_amount))

    # call the withdraw method of the account object for account_id passing in
    # the withdrawal_amount entered by the user
    accounts[account_id].withdraw(withdrawal_amount)

    # Ask the user to make a menu selection
    askForMenuOption(account_id)

def deposit(account_id):
    """
    Description: lets user deposit amount to account object associated with  
    the account_id
        :account_id : Int 
        :return : None : deposits amount to account
    """
    invalidEntry = True
    msg = "{} is not a number no deposit was made."
    # Ask user for the ammount to deposit making sure that it is a number
    while invalidEntry:
        try:
            deposit_amount = input("Enter the amount to withdraw: ")
            deposit_amount = int(deposit_amount)
            invalidEntry = False
        except:
            print(msg.format(deposit_amount))
    # call depoist_amount method on the accounts object for account_id passing
    # in the deposit_amount obtained from the user
    accounts[account_id].deposit(deposit_amount)
    # Ask the user to make a menu selection
    askForMenuOption(account_id)

def exitMenu():
    """ Description: Restarts the game by calling askForId() """
    askForId()

def callMenuAction(account_id,opt):
    """
    Description: Calls the pertinent function for the account_id based on the
        option selected by the user
        :input param
            :account_id : Int - account obtained from askForId method
            :opt : Int - option selected by user from askForMenuOption method 
            :return : None : calls method based on value of opt

    """
    if opt == 1:
        checkBalance(account_id)
    elif opt == 2:
        withdraw(account_id)
    elif opt == 3:
        deposit(account_id)
    else:
        exitMenu()

def askForMenuOption(account_id):
    """
    Description: Aks the user to enter the option they would like to call to
        action for the given account_id.
        :account_id : Int 
        :return : None : calls callMenuActionn passing in the account_id
                         and menuOption entered by user

    """
    invalidEntry = True
    msg = "{} is not a number no choice was made."
    while invalidEntry:
        try:
            menuOption = input("Enter a choice: ")
            menuOption = int(menuOption)
            invalidEntry = False
        except:
            print(msg.format(menuOption))
        else:
            if 0 < menuOption <= 4:
                break
            else:
                print("Option is out of range")
                invalidEntry = True

    callMenuAction(account_id,menuOption) 
    
def showMenu(account_id):
    """
    Description: Display the Menu options for the game for the account_id
        :account_id : Int 
        :return : None : calls askForMenuOption(account_id)

    """
    menu = {
        "1": "Check balance",
        "2": "withdraw",
        "3": "deposit",
        "4": "exit",
    }
    print("\n")
    for key in sorted(menu.keys()):
        print (key + ":" + menu[key])

    askForMenuOption(account_id)

def askForId():
    """
    Description: Gets the balance of the for the account object associated with 
    the account_id
        :account_id : Int 
        :return : None : calls askForMenuOption(account_id)

    """
    invalidEntry = True
    msg = "{} is not a number no choice was made."
    while invalidEntry:
        try:
            inp = input("Enter an account id: ")
            account_id = int(inp)
            invalidEntry = False
        except:
            print(msg.format(inp))
        else:
            if 0 <= account_id < 10:
                break
            else:
                print("Account id is out of range")
                invalidEntry = True
    
    showMenu(account_id)

if __name__ == "__main__":

    # initialize game by gettting account id
    askForId()
