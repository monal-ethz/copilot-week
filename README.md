# copilot-week

How to Run Cobol Program on codespaces:

- Install Brew
- Install dependencies
```
brew install gnucobol 
```
Compile each program separately as they will be linked together during runtime.
cobc -c main.cob -o main.o
cobc -c operations.cob -o operations.o
cobc -c data.cob -o data.o

Link and Create Executable: Link the object files together to create the final executable:
cobc -x main.o operations.o data.o -o accountsystem

Run the Program: Run the executable to start the account management system:
./accountsystem

Program starts with user input menu
--------------------------------
Account Management System
1. View Balance
2. Credit Account
3. Debit Account
4. Exit
--------------------------------
Enter your choice (1-4): 
