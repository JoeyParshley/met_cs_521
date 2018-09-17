"""
   Joey Parshley
   MET CS 521 O2
   17 APR 2018
   hw_6_7_3
   Description: Design a class named Account that contains:
                :   A private int data field named id for the account.
                :   A private float data field named balance for the account.
                :   A private float data field named annualInterestRate that 
                    stores the current interest rate.
                :   A constructor that creates an account with the specified
                    id (default 0), initial balance (default 100), and annual 
                    interest rate (default 0).
                :   The accessor and mutator methods for id , balance , and 
                    annualInterestRate .
                :   A method named getMonthlyInterestRate() that returns the 
                    monthly interest rate.
                :   A method named getMonthlyInterest() that returns the 
                    monthly interest.
                :   A method named withdraw that withdraws a specified amount 
                    from the account.
                :   A method named deposit that deposits a specified amount to 
                    the account.

                Write a test program that creates an Account object with an 
                account id of 1122, a balance of $20,000, and an annual interest 
                rate of 4.5%. Use the withdraw method to withdraw $2,500, use 
                the deposit method to deposit $3,000, and print the id, balance, 
                monthly interest rate, and monthly interest.

"""
from account import Account

if __name__ == "__main__":
    # create dictionay to hold the test account parameters
    account_dict = {
        "account_id": 1122,
        "balance": 20000,
        "int_rate": 0.045,
        "withdrawal_amount": 2500,
        "deposit_amount": 3000    
    }

    account = Account(
        account_dict["account_id"], account_dict["balance"], 
        account_dict["int_rate"])
    account.withdraw(account_dict["withdrawal_amount"])
    account.deposit(account_dict["deposit_amount"])

    print("The id is: {}".format(account.getId()))
    print("The balance is: ${:0,.2f}".format(account.getBalance()))
    print("The monthly interest rate is: {} %"
        .format(account.getMonthlyInterestRate() * 100))
    print("The monthly interest is: ${:0,.2f}"
        .format(account.getMonthlyInterest()))
