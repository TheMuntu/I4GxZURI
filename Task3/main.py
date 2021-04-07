import budget

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())

clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)

auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(f"The Current balance in {food.name} is {food.get_balance()}")
print(f"The Current balance is {clothing.name} is {clothing.get_balance()}")
print(f"The Current balance is {auto.name} is {auto.get_balance()}")