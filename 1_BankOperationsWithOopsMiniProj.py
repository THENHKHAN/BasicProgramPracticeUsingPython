
# Here we'll be making a Mini Projetc using oops functionality:

class Bank :
    bankName = "Noor Bank Of India "
    bankAddr = "ABC A-345 New Delhi 110023"

    # creating account
    def __init__(self,userName , UserPan ) :
        self.userName = userName 
        self.userPan = UserPan
        self.currentBalance = 0.0
        print (f"Hey, {self.userName} Your Account has been Created Successfully! ")

# check balance
    def checkBalance (self) :
        print(f" Your current balance is {self.currentBalance} ")

# deposite money
    def depositMoney (self , amount) :
        self.currentBalance = self.currentBalance + amount

        print (f" {amount} Rs is deposited in your account and current Balance is : {self.currentBalance} ") 

# withdraw money
    def withrawMoney (self , withDrawAmount) :
        if (self.currentBalance < withDrawAmount) :
            print(f" Sorry you have insufficient balance, Kindly try again.")

        else :
            self.currentBalance = self.currentBalance - withDrawAmount
            print (f" {withDrawAmount} Rs is withdrwan from your account and current Balance is : {self.currentBalance} ") 

# thank you note
    def thankYouNote (self ):
        print(f" Thank you for using our {self.bankName} - {self.userName}")

print(f"""
            ================================
               Welcome To {Bank.bankName} , {Bank.bankAddr} 
            ================================
    """)

print("""

        =======================================
        !!!!!!!!!!Register Yourself!!!!!!!!
        =======================================
    """)

userName = input ("Please enter your name : ")
panCard = input ("Please enter your pan card number  : ")

user = Bank (userName , panCard)

while True :
        
     
        print("""
                            1 -  Current Balance check
                            2 -  Add money
                            3 -  Withdraw Money
                            4 -  exit
            """)
        choice = int(input("\n ENTER YOUR CHOICE: "))
   
        if (choice == 1 ):
            user.checkBalance()

        elif (choice == 2) :
            amount = float (input("please enter your amount : "))
            user.depositMoney (amount)
            user.thankYouNote()

        elif (choice == 3):
            amount = float (input("please enter your amount : "))
            user.withrawMoney (amount)
            user.thankYouNote()

        elif (choice == 4):
                print("Please do come again!!!!")
                break

