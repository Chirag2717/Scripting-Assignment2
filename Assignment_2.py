# Author Name - Chirag Khurana
# Date - 15-11-2024

# Importing necessary libraries
import pandas as pd  
import matplotlib.pyplot as plt  

# Defining the BudgetTracker class
class BudgetTracker:
    def __init__(self):
        # Initializing income to zero
        self.income = 0
        
        # Creating an empty DataFrame with columns 'Category' and 'Amount' to store expenses
        self.expenses = pd.DataFrame(columns=['Category', 'Amount'])

    # Method to add income
    def add_income(self, amount):
        # Adding the given amount to total income
        self.income += amount
        # Printing confirmation message with formatted income amount
        print(f"Income added: ${amount:.2f}")

    # Method to add an expense
    def add_expense(self, category, amount):
        # Checking if the expense amount is positive
        if amount <= 0:
            print("Expense amount must be positive.")
            return
        
        # Creating a DataFrame for the new expense row
        new_row = pd.DataFrame({'Category': [category], 'Amount': [amount]})
        
        # Concatenating the new row with the existing expenses DataFrame
        # Using pd.concat() as .append() is deprecated in Pandas 2.0+
        self.expenses = pd.concat([self.expenses, new_row], ignore_index=True)
        
        # Printing confirmation message with formatted expense details
        print(f"Expense added: ${amount:.2f} in category {category}")

    # Method to generate a budget report
    def generate_report(self):
        # Calculating total expenses
        total_expenses = self.expenses['Amount'].sum()
        
        # Calculating remaining budget (income - total expenses)
        remaining_budget = self.income - total_expenses
        
        # Printing the budget summary report
        print("\n--- Budget Report ---")
        print(f"Total Income: ${self.income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Remaining Budget: ${remaining_budget:.2f}")

        # Checking if there are any expenses to visualize
        if not self.expenses.empty:
            # Creating a bar plot of expenses grouped by category
            self.expenses.groupby('Category')['Amount'].sum().plot(kind='bar')
            
            # Setting the title and labels for the plot
            plt.title('Expenses by Category')
            plt.xlabel('Category')
            plt.ylabel('Amount')
            
            # Displaying the plot
            plt.show()
        else:
            # If no expenses are recorded, display this message
            print("No expenses to report.")

# Example usage of the BudgetTracker class
if __name__ == "__main__":
    # Creating an instance of the BudgetTracker class
    tracker = BudgetTracker()
    
    # Adding income to the tracker
    tracker.add_income(5000)
    
    # Adding various expenses
    tracker.add_expense('Groceries', 300)
    tracker.add_expense('Rent', 1200)
    tracker.add_expense('Utilities', 150)
    
    # Generating the budget report and visualizing the expenses
    tracker.generate_report()
