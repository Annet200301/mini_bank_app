from datetime import datetime
from colorama import Fore, init
init(autoreset=True)  # Initialize colorama

def amount():
    while True:
        try:
            amt = float(input("Enter the amount to transfer: "))
            if amt > 0:
                return amt
            else:
                print("Amount must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def transfer_between_accounts():
    print("------------------------------------------------")
    print("          TRANSFER BETWEEN ACCOUNTS             ")
    print("------------------------------------------------")

    from_acc_no = input("From Account Number: ").strip()
    to_acc_no = input("To Account Number: ").strip()

    transfer_amount = amount()
    transfer_success = False
    updated_lines = []
    sender_found = receiver_found = False

    try:
        with open("accounts.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            data = line.strip().split(",")
            acc_no, name, balance = data[0], data[1], float(data[2])

            if acc_no == from_acc_no:
                sender_found = True
                if transfer_amount <= balance:
                    balance -= transfer_amount
                    updated_lines.append(f"{acc_no},{name},{balance}\n")
                    transfer_success = True
                else:
                    print(Fore.RED + "Insufficient balance for transfer.")
                    updated_lines.append(line)
            elif acc_no == to_acc_no:
                receiver_found = True
                balance += transfer_amount
                updated_lines.append(f"{acc_no},{name},{balance}\n")
            else:
                updated_lines.append(line)

        with open("accounts.txt", "w") as file:
            file.writelines(updated_lines)

        if transfer_success and sender_found and receiver_found:
            time = datetime.now().strftime("%d-%m-%Y %A %I:%M %p")
            with open("transactions.txt", "a") as trans_file:
                trans_file.write(f"from_acc: {from_acc_no}, to_acc: {to_acc_no}, transfer: {transfer_amount}, time: {time}\n")
            print(Fore.GREEN + f"Transfer successful! Amount: {transfer_amount}")
        elif not (sender_found and receiver_found):
            print(Fore.RED + "One or both account numbers not found.")

    except FileNotFoundError:
        print(Fore.RED + "accounts.txt file not found.")

    print("------------------------------------------------")
