"""
Bank Account Manager - Create a class called Account which
will be an abstract class for three other classes called
CheckingAccount, SavingsAccount and BusinessAccount. Manage
credits and debits from these accounts through an ATM style
program.
"""

class Account:

	def __init__(self, id):
		self.id = id


class CheckingAccount(Account):

	def __init__(self):
		