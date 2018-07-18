class Account:

	def __init__(self,owner,balance=0):
		self.owner = owner
		self.balance = balance

	def __str__(self):
		return f'Account owner: {self.owner}\nAccount balance: {self.balance}'

	def deposit(self, dep_amt):
		self.balance += dep_amt
		print(f"Your deposit of ${dep_amt} has been accepted")

	def withdraw(self,wd_amt):
		if self.balance >= wd_amt:
			self.balance -= wd_amt
			print(f"You have withdrawn {wd_amt}")

		else:
			print("You do not have sufficient funds to make the withdrawal you've requested.")

acct1 = Account('Tyler',100)
print(acct1)
#acct1.deposit(50)
#acct1.withdraw(200)