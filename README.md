# copilot-week

Program starts with user input menu
--------------------------------
Account Management System
1. View Balance
2. Credit Account
3. Debit Account
4. Exit
--------------------------------
Enter your choice (1-4): 

## Python files

# Overview of main.py

The main.py file serves as the entry point for the Account Management System. It provides a user interface to interact with the system and perform various operations such as viewing the balance, crediting the account, and debiting the account. Below is a brief explanation of the key components and functionality:

Imports:

DataProgram: Manages reading and writing the balance to a file.
OperationsProgram: Handles different operations (view balance, credit, debit) on the balance.
Main Function:

Initializes instances of DataProgram and OperationsProgram.
Uses a loop to continuously display a menu to the user until they choose to exit.
Processes user input to perform the corresponding operations:
View Balance (1): Displays the current balance.
Credit Account (2): Prompts the user to enter an amount to credit and updates the balance.
Debit Account (3): Prompts the user to enter an amount to debit and updates the balance if sufficient funds are available.
Exit (4): Exits the program.
Handles invalid choices by displaying an error message.
Execution Check:

Ensures that the main() function is executed when the script is run directly.
This file orchestrates the interaction between the user and the underlying business logic implemented in the OperationsProgram and DataProgram classes.