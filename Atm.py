class atm():
    def __init__(self, cardNo, pinNo):
       self.cardNo = cardNo
       self.pinNo = pinNo
       self.balance = 0

    def CashWithdrawl(self):
        print("the transaction was a success")

    def BalanceEnquiry (self):
        print("your balance is ",self.balance)

card = input("Enter  your card no ")
pin = input("Enter your pin ")

userName=atm(card, pin)

userName.CashWithdrawl()
userName.BalanceEnquiry()