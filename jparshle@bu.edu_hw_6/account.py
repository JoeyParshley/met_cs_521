
class Account():
    """ 

    Account class

        :params :   id                  - Int - account is default - 0
                :   balance             - Float - account balance default - 0
                :   annualInterestRate  - Float - annual interewst rate 
                                          defauult - 1
        :returns:   account object

    """
    def __init__(self, id=0, balance = 100, annualInterestRate = 0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate


    def __str__(self):
        s_id = str(self.__id)
        s_balance = str(self.__balance)
        s_annualInterestRate = str(self.__annualInterestRate)

        return "Account id = {0},"\
            " balance = {1},"\
            " interest rate = {2}".format(s_id, s_balance, s_annualInterestRate)

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getBalance(self):
        return self.__balance

    def setBalance(self, balance):
        self.__balance = balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def setAnnualInterestRate(self, annualInterestRate):
        self.__balance = annualInterestRate

    def getMonthlyInterestRate(self):
        """ Monthly interest based on annul Interes / 12 """
        return self.__annualInterestRate / 12

    def getMonthlyInterest(self):
        """ Get monthly interest """
        return self.getBalance() * self.getMonthlyInterestRate()

    def withdraw(self, amount):
        """ Withdraw amount """
        self.setBalance(self.getBalance() - amount)

    def deposit(self, amount):
        """ Deposit amount """
        self.setBalance(self.getBalance() + amount)

    def __str__(self):
        return "Account - id: "  + str(self.__id) +  \
            " balance = "  + str(self.__balance) +  \
            " Rate = "  + str(self.__annualInterestRate)
