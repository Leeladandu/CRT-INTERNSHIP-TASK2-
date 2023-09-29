import os
import csv
import datetime
#define the filename for datastorage
DATA_FILE="budget_data.csv"
#Intialize an empty dictionary to store budget data
budget_data={
"income":0,
"expenses":[],
}
#to load budget data from the file
def load_budget_data():
  if os.path.exists(DATA_FILE):
     with open(DATA_FILE,mode="r",newline="")as file:
       reader=csv.DictReader(file)
       for row in reader:
        if row["type"]=="income":
          budget_data["income"]=float(row["amount"])
        elif row["type"]=="expense":
          budget_data["expenses"].append({"category":row["category"],"amount":
          float(row["amount"]),"date":row["date"]
})
#to save budget data to the file
def save_budget():
  with open(DATA_FILE,mode="w",newline="")as file:
   fieldnames = ["type", "category", "amount", "date"]
   writer=csv.DictWriter(file,fieldnames=fieldnames)
   writer.writeheader()
#write income data
   writer.writerow({"type":"income","amount":budget_data["income"],"category":"","date":""})
#write expense data
for expense in budget_data["expenses"]:
   writer.writerow({
   "type":"expense",
   "category":expense["category"],
   "amount":expense["amount"],
   "date":expense["date"]
    })
# to add an income entry
def add_income():
   try:
    income_amount=float(input("Enter income amount:$"))
    budget_data["income"]+=income_amount
    print(f"income of ${income_amount:.2f}added successfully.")
    save_budget_data()
   except ValueError:
       print("Invalid input.Please enter a valid amount.")
 # to add an expense entry
def add_expense():
   category=input("enter expense category:")
   try:
     expense_amount=float(input("enter expense amount:$"))
     current_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     budget_data["expenses"].append({
      "category":category,
      "amount":expense_amount,
      "date":current_date
     })
     budget_data["income"]-=expense_amount
     print(f"Expense of $ {expense_amount:.2f} in '{category}' category added successfully.")
     save_budget_data()
   except ValueError:
     print("Invalid input.Please enter a valid amount.")
#Function to display the budget summary
def display_budget_summary():
   total_expenses=sum(expense["amount"] for expense in budget_data["expenses"])
   remaining_budget=budget_data["income"]-total_expenses
   print("\n Budget Summary")
   print("--------")
   print(f"Income:${budget_data['income']:.2f}")
   print(f"Remaiining Budget:${remaining_budget:.2f}")
#Function to categorize and analyze expenses
def analyze_expenses():
    expense_categories={}
    for expense in budget_data["expenses"]:
      category=expense["category"]
      amount=expense["amount"]
    if category in expense_categories:
      expense_categories[category]+=amount
    else:
      expense_categories[category]=amount
    print("\n Expense Analysis")
    print("---------")
    for category in expense_categories.items():
      print(f"{category}: ${amount:.2f}")
#main loop
def main():
    load_budget_data()
    while True:
        print("\n Budget Tracker Menu")
        print("________")
        print("1.Add Income amount")
        print("2.Add Expense amount")
        print("3.Display summary")
        print("4.Analyze Expenses")
        print("5.Exit")
        choice=input("Select an option(1/2/3/4/5):")
        if choice=="1":
          add_income()
        elif choice=="2":
          add_expense()
        elif choice=="3":
          display_budget_summary()
        elif choice=="4":
           analyze_expenses()
        elif choice=="5":
           print("ExitinG Budget Tracker.Have a great day!")
           break
        else:
           print("Invalid choice.please select a valid option(1/2/3/4/5).")
if __name__ == "__main__":
      main()
