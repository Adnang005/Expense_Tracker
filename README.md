# Expense_Tracker
#  DecodeLabs Expense Tracker

##  Project Overview

The problem was to create a simple **Expense Tracker** that accepts multiple expenses from the user and calculates the total amount spent. I solved this by creating an `ExpenseTracker` class that stores the total expenses and their history using Python lists.

##  How I Solved the Problem

The main concept used in this project is the **Accumulator Pattern**: `self.total = self.total + expense`. Every time the user enters a valid expense, it is added to the previous total. I also stored each expense and its running total in separate lists so the complete transaction history could be displayed.

##  Functions and Features Used

I used the `__init__()` constructor to initialize the total and lists, `add_expense()` to validate and process expenses, `show_history()` to display all transactions, and `main()` to control the application. The program uses `float()` for number conversion, `append()` for storing data, `while` for continuous input, and `if/else` for validation.

##  Input Handling

To make the program reliable, I used `try/except` to handle invalid input such as letters instead of numbers. I also checked that expenses are greater than zero. The user can enter `done` to stop the input loop, which works as a **sentinel value**.

##  Learning Outcome

Through this project, I practiced **Object-Oriented Programming, lists, loops, functions, input validation, exception handling, string formatting, and the Accumulator Pattern**. This project helped me understand how to process multiple inputs and maintain a running total in a real-world application.
