from datetime import datetime
import os
from colorama import Fore,Back,Style,init
init(autoreset=True) 
#"pip install colorama" run in command prompt
#=================================================================================
def users_id_creation():
    if not os.path.exists("ustomer_details.txt") or os.path.getsize("users.txt") == 0:
        return "U001"
    with open("customer_details.txt", "r") as user_file:
        return f"U{int(user_file.readlines()[-1].split(",")[-1][1:]) + 1:04}"
#==================================================================================
def input_validation(prompt):
    while True:
        value =  input(prompt).strip()
        if value :
            return value
        else:
            print(Fore.LIGHTRED_EX+"input can't empty")
#==staff menu======================================================================
def staff_menu():
    while True:
        print("===============MENU OPTION===============")
        print("1:adding new customer and account creation")
        print("2:Deposits")
        print("3:Withdrawals")
        print("4:Check balances")
        print("5:Money transfer between accounts")
        print("6:Transaction history")
        print(Fore.LIGHTRED_EX+"7:exit")
        try:
            choice =int(input("enter the option you choose:"))
        except ValueError:
            print(Fore.LIGHTRED_EX+" your chosen option is invalid")
        if choice == (1):
            new_account_creation()
        elif choice == 2:
            deposits()
        elif choice == 3:
            withdrawal()
        elif choice == 4:
            balance_check()
        elif choice == 5:
            transfer_between_accounts()   
        elif choice == 6:
            transaction_history()
        elif choice ==7:
            exit()
        else :
            print(Fore.LIGHTRED_EX+"INVALID INPUT")
#===customer menu=======================================================================
def  customer_menu():
    while True:
        print("===============MENU OPTION===============")
        print("1:Deposit")
        print("2:Withdrawal")
        print("3:Check balance")
        print("4:Transfer between accounts")
        print("5:Transaction history")
        print(Fore.LIGHTRED_EX+"6:Exit")
        try:
            choice=int(input("enter the option you choose:"))
        except ValueError:
            print(Fore.LIGHTRED_EX+" your chosen option is invalid")
        if choice == 1:
            deposits()
        elif choice == 2:
            withdrawal()
        elif choice == 3:
            balance_check()
        elif choice == 4:
            transfer_between_accounts()   
        elif choice == 5:
            transaction_history()
        elif choice==6:
            exit()
        else :
            print(Fore.LIGHTRED_EX+"INVALID INPUT")
#---------------------------------------------Login -----------------------------------------  
def customer_login():
    while True:
        print(Fore.LIGHTMAGENTA_EX+"For Security purpose you have to login ")
        username = input("Enter your username:").strip()
        password = input('Enter your password:').strip()
        login_successful=False
        try :
            with open ("users.txt","r") as User_file:
                for lines in User_file:
                    users=lines.strip().split(",")
                    if users[0]==username and users[1]==password:
                        print(Fore.LIGHTYELLOW_EX+"-----LOGIN SUCCESSFUL-----")
                        login_successful=True
                        customer_menu()
                        break
            if not login_successful:
                print(Fore.LIGHTRED_EX+"-----LOGIN FAILED!!!!!!!-----")
        except FileNotFoundError:
            print (Fore.LIGHTRED_EX+"Errroooorrrr ....users.txt  file not found!!!!!!!!!!! ")
#ADMIN LOGIN
def admin_login():
    admin_id= "Authoritative"
    admin_password="author123"
    #with open("users.txt","a")as file:
        #file.write(f"{admin_id},{admin_password}")
    while True:
        print(Fore.LIGHTMAGENTA_EX+"For Security purpose you have to login ")
        username = input("Enter your administrative username:").strip()
        password = input('Enter your password:').strip()
        if username==admin_id and password==admin_password:
                print(Fore.LIGHTYELLOW_EX+"-----LOGIN SUCCESSFUL-----")
                print("---------------------------------------------")
                staff_menu()
        else:
            print(Fore.LIGHTRED_EX+"username or password is wrong")
             
#USER DETAILS INPUT AND NEW ACCOUNT CREATION########################################################################
def user_details_input():
    print ("-------------------------------")
    print ("  CUSTOMER INFORMATION INPUT    ")
    print ("-------------------------------")

    check_user_name=set()
    try:
        with open ("users.txt","r") as file:
            for line in file:
                if "," in line:
                    check_user_name.add(line.strip().split(",")[0])
    except FileNotFoundError:
        pass
    full_name =input_validation("Enter the full name:")
    while True:
        username= input_validation("enter the user name:").strip()
        if username in check_user_name:
            print (Fore.LIGHTRED_EX+'oops!!  user name already exist try a new one ')
        else:
            break
    address=input_validation("enter the address:")
    nic=input_validation("enter the nic number :")
    phone_number=input_validation("enter the phone number:")
    password=input_validation("enter the password:")
    user_id=users_id_creation()

    with open ("users.txt","a")as file:
        file.write(f"{username},{password}\n")

    with open("customer_details.txt","a")as file:
        file.write(f"{username},{password},{nic},{address},{phone_number},{full_name},{user_id}\n")
    print(Fore.LIGHTYELLOW_EX+'SUCCESSFULLY SAVED THE CUSTOMER DETAILS ')
    print("========================================")
    return[username, password, nic, address, phone_number,full_name]
#------------------------------------------------------------------------------------------------------------------------------
#                      NEW ACCOUNT CREATION
#------------------------------------------------------------------------------------------------------------------------------
def new_account_creation():
    customer_details=user_details_input()
    account_number=(f"ACC{abs(hash(customer_details[2]))}UIC")
    while True:
        try:
            balance=int(input("Enter the initial amount to create an account:"))
            if balance >= 1000:#initial balance must be greater than 1000
                break
            else:
                print(Fore.LIGHTRED_EX+"initial balance must be greater than 1000")
        except ValueError:
            print('ENTER A VALID  NUMERICAL AMOUNT')

    with open ("accounts.txt","a")as file:
        file.write(f"{account_number},{customer_details[0]},{balance},\n")

    print(f"The account Number is: {account_number}")
    print(Fore.LIGHTYELLOW_EX+"Account created successfully! \n")

#BALANCE CHECK #####################################################################################################
def balance_check():
    print("------------------------------------------------------------------------------------------------")
    print("                              ACCOUNTS  DETAILS                                                   ")
    print("------------------------------------------------------------------------------------------------")

    username=input_validation("Enter the user name:").strip()
    user_found=False
    with open ("accounts.txt","r")as file:
        for line in file:
            data=line.strip().split(",")
            if data[1]==username :
                print(f"{data[1]}:-:= Account numbers:-{(data[0])}\t,balance is:-{data[2]}\n")
                user_found=True
    print("=============================================================================================\n")
                
    if  not user_found :
        print(Fore.LIGHTRED_EX+"please enter a user name")
#FUNCTIONS RELATED TO WITHDRAWEL AND DEPOSITES#############################################################################
def amount():
    while True:
        try:
            Amount= float(input("enter the amount:"))
            if Amount>0:
                return Amount
                break
            else:
                print("amount must be positive:(")
        except ValueError:
            print ("Enter Number only :(")
#DEPOSITES----------------------------------------------------------------------------------------------------------
def deposits():
    print("---------------------------------------")
    print('              DEPOSIT                  ')
    print("---------------------------------------")
    depo=False
    account_no=input("enter the account number:").strip()
    with open("accounts.txt","r")as file:
        lines = file.readlines()
    updated_lines=[]

    for line in lines:
        data=line.strip().split(",")

        if data[0]==account_no:
            deposite_amount=amount()
            balances=float(data[2])
            new_balances=balances + deposite_amount
            updated_lines.append(f"{account_no},{data[1]},{new_balances}\n")
            depo=True

            time = datetime.now().strftime("%d-%m-%Y %A %I %M %p")
            with open("Transactions.txt","a") as  trans_file:
                trans_file.write(f"{account_no},{balances},deposit,{new_balances},{time}\n")
                print(f"deposite successful:) and your new balance is{new_balances}")
        else:
            updated_lines.append(line)
    with open ("accounts.txt","w") as file:
        file.writelines(updated_lines)
    if not depo:
        print(Fore.LIGHTRED_EX+"Account not found")
    print("=================================================================================")
#--------------------------------------------------------------------------------------------------------------------
def withdrawal():

    print("-----------------------------------------------------")
    print("                  Withdrawel                         ")
    print("-----------------------------------------------------")
    account_number=input_validation("Enter the account number:").strip()
    username=input_validation("Enter the username of this account:").strip()
    password=input_validation("Enter the password of the above username:").strip()
    withdraw_amount=amount()
    wdraw=False
    updated_lines=[]
    details=False
    

    with open("accounts.txt","r")as file:
        lines = file.readlines()
        for line in lines:
            data=line.strip().split(",")
            if data[0]==account_number:
                if data[1]==username:
                    balances=float(data[2])
                with open('users.txt',"r")as file:
                    lines=file.readlines()
                    for line in lines:
                        words=line.strip().split(",")
                        if data[1]==username and words[1]==password:
                            details=True    
                    
                    if not details:
                        print(Fore.LIGHTRED_EX+"you can't withdraw because username or password of this account must be wrong !")
                        break

                if withdraw_amount< balances:
                    new_balances = balances - withdraw_amount
                    updated_lines.append(f"{account_number},{data[1]},{new_balances}\n")
                    wdraw=True

                    time = datetime.now().strftime("%d-%m-%Y %A %I %M %p")
                    with open("Transactions.txt","a") as  transaction_file:
                        transaction_file.write(f"{account_number},{balances},withdrawel,{new_balances},{time}\n")
                        print(f"withdrawel successful:) and your new balance is{new_balances}")
                else:
                    print(Fore.LIGHTRED_EX+"Insufficient balances!")
                    updated_lines.append(line)
            else:
                updated_lines.append(line)
        with open("accounts.txt","w")as file:
            file.writelines(updated_lines)
                
        if  not wdraw :
            print(Fore.LIGHTRED_EX+"Account not found")
    print("==================================================================================================")
#TRANSFER BETWEEN ACCOUNTS########################################################################################
def transfer_between_accounts():
    print("------------------------------------------------")
    print("          TRANSFER BETWEEN ACCOUNTS          ")
    print("-------------------------------------------------")
    from_acc_no=input ("type:from which account number you want to transfer the amount:").strip()
    to_acc_no=input ("type:to which account number you want to transfer the amount:").strip()
    from_found=False
    to_found=False
    transfer_amount=0
    updated_lines=[]
    transfer_amount = amount()
    try:
        with open("accounts.txt", "r") as file:
            lines = file.readlines()
        for line in lines:
            data = line.strip().split(",")
            if data[0] == from_acc_no:
                from_found=True
                sender_username=data[1]
                sender_balance = float(data[2])
            if data[0]==to_acc_no:
                to_found=True
                receiver_username=data[1]
                receiver_balance=float(data[2])
        if not from_found or not to_found:
            print(Fore.LIGHTRED_EX + "One or both account numbers not found.")
            return
        if transfer_amount > sender_balance:
            (Fore.LIGHTRED_EX + "Not sufficient balance for transfer.")


        for line in lines:
            data = line.strip().split(",")
            if data[0] == from_acc_no:
                new_balance = sender_balance - transfer_amount
                updated_lines.append(f"{from_acc_no},{data[1]},{new_balance}\n")
            elif data[0] == to_acc_no:
                new_balance = receiver_balance + transfer_amount
                updated_lines.append(f"{to_acc_no},{data[1]},{new_balance}\n")
            else:
                updated_lines.append(line)

        with open("accounts.txt", "w") as file:
            file.writelines(updated_lines)

        time = datetime.now().strftime("%d-%m-%Y %A %I:%M %p")
        with open("transactions.txt", "a") as file:
            file.write(f"{from_acc_no}, to_acc: {to_acc_no}, transfer: {transfer_amount}, new_balance: {sender_balance - transfer_amount}, time: {time}\n")

        print(Fore.LIGHTYELLOW_EX + f"Transfer successful. New balance for {from_acc_no}: {sender_balance - transfer_amount}")

    except FileNotFoundError:
        print(Fore.LIGHTRED_EX + "accounts.txt not found.")
        print("-------------------------------------------------------------------------------------")

################################################################################################################
def transaction_history():
    account_number = input("Enter your account number to see you history: ").strip()
    found=False
    try:
        with open("transactions.txt", "r") as transaction_file:
            print(f"{'account_number':<35}{'current balance':<20}{'deposite/withdrawel':<25}{'amount':<15}{'time'}\n")
            for line in transaction_file:
                transaction_data = line.strip().split(',')
                if account_number == transaction_data[0]:
                    print(f"{transaction_data[0]:<35}{transaction_data[1]:<20}{transaction_data[2]:<25}{transaction_data[3]:<15}{transaction_data[4]}\n")
                    found=True
                
        if not found:
            print(Fore.LIGHTRED_EX+"no transaction found for this account")
    except FileNotFoundError:
        print(Fore.LIGHTRED_EX+"Transaction file not found ")
#######################################################################################################
def banking_app():
    while True:
        try:
            print(Fore.BLUE+"welcome to our banking system----------\n1:Admin\n2:Customer\n3:Exit")
            choice=int(input_validation("enter the option you choose(1-3):"))
            print("\n")
            if choice==1:
                admin_login()
            elif choice==2:
                customer_login()
            elif choice==3:
                print("-----THANKYOU-----")
                exit()
            else:
                print("Enter the choice between(1-3)")
        except ValueError:
            print(Fore.LIGHTRED_EX+" your option is invalid")
banking_app()
        





