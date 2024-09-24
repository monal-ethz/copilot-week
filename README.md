# Python Programm

## Overview of main.py

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

## Overview of operations.py
The operations.py file contains the OperationsProgram class, which handles various operations on an account balance. This class interacts with the DataProgram class to read and write the balance. Below is a brief explanation of the key components and functionality:

Initialization:

The OperationsProgram class is initialized with an instance of DataProgram, which manages the balance data.
Execute Method:

The execute method takes an operation_type argument and calls the corresponding method (total, credit, or debit) based on the operation type.
If the operation type is invalid, it prints an error message.
Total Method:

The total method reads the current balance using data_program.read_balance() and prints it.
Credit Method:

The credit method prompts the user to enter an amount to credit.
It reads the current balance, adds the credit amount, and writes the new balance using data_program.write_balance().
It then prints the new balance.
Debit Method:

The debit method prompts the user to enter an amount to debit.
It reads the current balance and checks if there are sufficient funds.
If sufficient funds are available, it subtracts the debit amount and writes the new balance using data_program.write_balance().
It then prints the new balance.
If there are insufficient funds, it prints an error message.
This file provides the core functionality for performing operations on the account balance, including viewing the balance, crediting the account, and debiting the account.

## Overview of data.py
The data.py file contains the DataProgram class, which is responsible for managing the account balance data. This class handles reading the balance from a file and writing the balance to a file. Below is a brief explanation of the key components and functionality:

- Initialization:
-- The DataProgram class is initialized with a filename (default is 'balance.dat') and a default balance of 1000.00.
-- It calls the read_balance() method to read the balance from the file during initialization.

- Read Balance Method:
-- The read_balance() method attempts to read the balance from the specified file.
-- If the file is not found, it calls the write_balance() method to create the file with the default balance.
It returns the current balance.
Write Balance Method:

The write_balance() method takes a balance as an argument and writes it to the specified file.
It updates the internal balance attribute and writes the balance to the file in a formatted manner.
This file provides the essential functionality for persisting the account balance data, ensuring that the balance is read from and written to a file as needed.