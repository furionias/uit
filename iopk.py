
def find_number(matrix, target, val):
	for i in range(len(matrix)):
		if matrix[i]+[i] == target:
			val += len(matrix)
			return val
			print(i)

find_number(matrix=[
[0, 0, 0, 1, 0, 0,0,],
[000, 0, 0, 0, 0, 0, 0,]

	], target= 1, val=0)





import random
import time
class  finance_management():

	def __init__(self, initial_value, tax, profit, income, debt):
		self.initial_value = initial_value
		self.tax = tax 
		self.profit = profit 
		self.income = income
		self.debt = debt


	def monthly_tax(self):
		rand = random.randrange(1, 100)
		print(f"Your tax payment is {rand} ")
		self.initial_value -= rand
		if self.initial_value == 0:
			print(f"You will have {self.value} left")
			self.tax -= 3

		else: 
			print(self.initial_value)
   
    def gain(self):  
        print("You have gained more money")	
        self.profit += 10
        self.initial_value += 10


io = finance_management(tax=10, initial_value=100, income=45, profit=0, debt=0)
x = 100

print(x<<90)
print(x<<3)


