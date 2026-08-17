"""
PROJECT 2: EXPENSE TRACKER
DecodeLabs - Python Developer (Batch 2026)
THE ACCUMULATOR PATTERN:
total = total + new_expense
Every new expense adds to the running total!
"""

class ExpenseTracker:
    def __init__(self):
        # Starting from zero
        self.total = 0.0
        self.expenses = []
        self.running_totals = []  # Track history of totals
    
    def add_expense(self, amount):
        try:
            # Convert string to number
            expense = float(amount)
            
            if expense <= 0:
                print(" Must be greater than zero!")
                return
            
            # SHOW BEFORE ACCUMULATION
            old_total = self.total
            print(f"\n BEFORE ACCUMULATION:")
            print(f"   Old Total: ${old_total:.2f}")
            print(f"   New Expense: ${expense:.2f}")
            
            # THE ACCUMULATOR PATTERN
            # total = total + new_expense
            self.total = self.total + expense  # ← THIS IS THE KEY!
            
            # Store expense history
            self.expenses.append(expense)
            self.running_totals.append(self.total)
            
            # SHOW AFTER ACCUMULATION
            print(f"\n AFTER ACCUMULATION:")
            print(f"   New Total: ${self.total:.2f}")
            print(f"   Added: ${expense:.2f} to the running total!")
            print(f"   Expense recorded successfully!")
            
            # CONFIRMATION STATEMENT
            print(f"\n CONFIRMATION: Expense of ${expense:.2f} has been added!")
            print(f"   Your new total is: ${self.total:.2f}")
            
        except ValueError:
            print(" Invalid input! Enter a number.")
    
    def view_total(self):
        """Display final total"""
        print(f"\n Total Spent: ${self.total:.2f}")
    
    def show_history(self):
        """Show complete transaction history"""
        if not self.expenses:
            print("\n No expenses recorded yet!")
            return
        
        print("\n" + "="*60)
        print(" EXPENSE HISTORY WITH ACCUMULATION")
        print("="*60)
        print(f"{'#':<4} {'Expense':<12} {'Running Total':<15}")
        print("-"*60)
        
        for i in range(len(self.expenses)):
            print(f"{i+1:<4} ${self.expenses[i]:<10.2f} ${self.running_totals[i]:<14.2f}")
        
        print("-"*60)
        print(f"{'FINAL':<4} {'':<12} ${self.total:<14.2f}")
        print("="*60)

def main():
    tracker = ExpenseTracker()
    
    print("="*60)
    print(" EXPENSE TRACKER")
    print("="*60)
   # print("THE ACCUMULATOR PATTERN:")
    #print("total = total + new_expense")
   # print("-"*60)
    print("Enter expenses (type 'done' to finish):\n")
    
    # Continuous input loop
    while True:
        # INPUT: Get expense
        user_input = input("$ ")
        
        # THE KILL SWITCH: Sentinel value
        if user_input.lower() == 'done':
            break
        
        # PROCESS: Add expense with confirmation
        tracker.add_expense(user_input)
    
    # OUTPUT: Show final summary
    print("\n" + "="*60)
    print(" FINAL SUMMARY")
    print("="*60)
    
    # Show complete history
    tracker.show_history()
    
    print("\n Goodbye!")

if __name__ == "__main__":
    main()