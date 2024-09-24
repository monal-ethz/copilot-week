
from data import DataProgram
from operations import OperationsProgram

def main():
    data_program = DataProgram()
    operations_program = OperationsProgram(data_program)
    continue_flag = 'YES'

    while continue_flag == 'YES':
        print("--------------------------------")
        print("Account Management System")
        print("1. View Balance")
        print("2. Credit Account")
        print("3. Debit Account")
        print("4. Exit")
        print("--------------------------------")
        user_choice = input("Enter your choice (1-4): ").strip()

        if user_choice == '1':
            operations_program.execute('TOTAL')
        elif user_choice == '2':
            operations_program.execute('CREDIT')
        elif user_choice == '3':
            operations_program.execute('DEBIT')
        elif user_choice == '4':
            continue_flag = 'NO'
        else:
            print("Invalid choice, please select 1-4.")

    print("Exiting the program. Goodbye!")

if __name__ == "__main__":
    main()