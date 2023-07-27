#bank operation using OOP
class Bank:
  Bankname = "WELLS FARGO"
  Address = "A23,BLR,India"  #static variable

  #account creation
  def __init__(self, username, PAN):
    self.username = username
    self.PAN = PAN
    self.balance = 0.0
    print(f'Hello {self.username} ,your acount has been created successfully')

  #deposit

  def deposit(self, amount):
    self.balance = self.balance + amount
    print(f"{amount} deposited successfully")

  def withdraw(self, amount):
    if amount <= self.balance:
      self.balance = self.balance - amount
      print(f'{amount} withdrawn successfully')

    else:
      print("insufficient balance")

  def ministatement(self):
    print(f"Your account balance is {self.balance}")


print(f"Welcome to {Bank.Bankname}", {Bank.Address})
username = input("enter your name: ")
PAN = input("enter PAN card number: ")

b = Bank(username, PAN)
#infinite loop
while True:
  print("please select any option")
  print("1.deposit\n 2.Withdraw\n3.mini statement\n4.stop")
  option = int(input(""))

  if option == 1:
    amount = float(input())

    b.deposit(amount)

  if option == 2:
    amount = float(input("enter withdrawl amount"))
    b.withdraw(amount)

  if option == 3:
    b.ministatement()

  if option == 4:
    print("Thanks For choosing WELLS!")
    break

  else:
    print("invalid option pls select a valid option")
