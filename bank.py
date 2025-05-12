from datetime import datetime
#==================================================================================
def input_validation(prompt):
    while True:
        value =  input(prompt).strip()
        if value :
            return value
        else:
            print("input can't empty")
#==staff menu======================================================================
def staff_menu():
    print("===============MENU OPTION===============")
    print("1:adding new customer and account creation")
    print("2:Deposits")
    print("3:Withdrawals")
    print("4:Check balances")
    print("5:Money transfer between accounts")
    print("6:Transaction history")
    print("7:exit")
    while True:
        try:
            choice =int(input("enter the option you choose:"))
            break
        except ValueError:
            print(" your chosen option is invalid")
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
    else :
        print('thank you for using our banking sercices')
        exit()
#===customer menu=======================================================================
def  customer_menu():
    print("===============MENU OPTION===============")
    print("1:Deposit")
    print("2:Withdrawal")
    print("3:Check balance")
    print("4:Transfer between accounts")
    print("5:Transaction history")
    print("6:Exit")
    while True:
        try:
            choice=int(input("enter the option you choose:"))
            break
        except ValueError:
            print(" your chosen option is invalid")
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
    else :
        print('thank you for using our banking sercices')
        exit()
#---------------------------------------------Login -----------------------------------------  
def customer_login():
    while True:
        username = input("Enter your username:").strip()
        password = input('Enter your password:').strip()
        login_successful=False
        try :
            with open ("users.txt","r") as User_file:
                for lines in User_file:
                    users=lines.strip().split(",")
                    if len(users)==2 and users[0]==username and users[1]==password:
                        print("-----LOGIN SUCCESSFUL-----")
                        login_successful=True
                        customer_menu()
                        break
            if not login_successful:
                print("-----LOGIN FAILED!!!!!!!-----")
        except FileNotFoundError:
            print ("Errroooorrrr ....users.txt  file not found!!!!!!!!!!! ")
#ADMIN LOGIN
def admin_login():
    admin_id= "Authoritative"
    admin_password="author123"
    while True:
        print("For Security purpose you have to login ")
        username = input("Enter your administrative username:").strip()
        password = input('Enter your password:').strip()
        if username==admin_id and password==admin_password:
                print("-----LOGIN SUCCESSFUL-----")
                print("--------------------------")
                staff_menu()
        else:
            print("username or password is wrong")
             
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
    while True:
        username= input_validation("enter the name:").strip()
        if username in check_user_name:
            print ('oops!!  user name already exist try a new one ')
        else:
            break
    address=input_validation("enter the address:")
    nic=input_validation("enter the nic number :")
    phone_number=input_validation("enter the phone number:")
    password=input_validation("enter the password:")


    with open ("users.txt","a")as file:
        file.write(f"{username},{password}\n")

    with open("customer_details.txt","a")as file:
        file.write(f"username:{username}\npassword:{password}\nNIC:{nic}\naddress:{address}\nphone number:{phone_number}\n")
        file.write("-----------------------------------------------------------------------------\n")
    print('SUCCESSFULLY SAVED THE CUSTOMER DETAILS ')
    print("========================================")
    return[username, password, nic, address, phone_number]
#------------------------------------------------------------------------------------------------------------------------------
#                      NEW ACCOUNT CREATION
#------------------------------------------------------------------------------------------------------------------------------
def new_account_creation():
    global customer_details
    customer_details=user_details_input()
    account_number=(f"ACC{abs(hash(customer_details[2]))}UIC")
    while True:
        try:
            balance=int(input("Enter the initial amount to create an account:"))
            if balance >= 1000:#initial balance must be greater than 1000
                break
            else:
                print("initial balance must be greater than 1000")
        except ValueError:
            print('ENTER A VALID  NUMERICAL AMOUNT')

    with open ("accounts.txt","a")as file:
        file.write(f"{account_number},{customer_details[0]},{balance},\n")

    print(f"The account Number is: {account_number}")
    print("Account created successfully! \n")

#BALANCE CHECK #####################################################################################################
def balance_check():
    print("------------------------------------------------------------------------------------------------")
    print("                              ACCOUNTS  DETAILS                                                   ")
    print("------------------------------------------------------------------------------------------------")

    username=input ("Enter the user name:").strip()
    user_found=False
    with open ("accounts.txt","r")as file:
        for line in file:
            data=line.strip().split(",")
            if data[1]==username :
                print(f"{data[1]}:-:= Account numbers:-{(data[0])}\t,balance is:-{data[2]}\n")
                user_found=True
    print("=============================================================================================\n")
                
    if  not user_found :
        print("please enter a user name")
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
        print("Account not found")
    print("=================================================================================")
#--------------------------------------------------------------------------------------------------------------------
def withdrawal():

    print("-----------------------------------------------------")
    print("                  Withdrawel                         ")
    print("-----------------------------------------------------")
    account_number=input("Enter the account number:").strip()
    wdraw=False
    updated_lines=[]

    with open("accounts.txt","r")as file:
        lines = file.readlines()
        for line in lines:
            data=line.strip().split(",")
            if data[0]==account_number:
                withdraw_amount=amount()
                balances=float(data[2])

                if withdraw_amount< balances:
                    new_balances = balances - withdraw_amount
                    updated_lines.append(f"{account_number},{data[1]},{new_balances}\n")
                    wdraw=True

                    time = datetime.now().strftime("%d-%m-%Y %A %I %M %p")
                    with open("Transactions.txt","a") as  transaction_file:
                        transaction_file.write(f"{account_number},{balances},withdrawel,{new_balances},{time}\n")
                        print(f"withdrawel successful:) and your new balance is{new_balances}")
                else:
                    print("Insufficient balances!")
                    updated_lines.append(line)
            else:
                updated_lines.append(line)
        with open("accounts.txt","w")as file:
            file.writelines(updated_lines)
                
        if  not wdraw :
            print("Account not found")
    print("==================================================================================================")
#TRANSFER BETWEEN ACCOUNTS########################################################################################
def transfer_between_accounts():
    print("------------------------------------------------")
    print("          TRANSFER BETWEEN ACCOUNTS          ")
    print("-------------------------------------------------")
    from_acc_no=input ("type:from which account number you want to transfer the amount:").strip()
    to_acc_no=input ("type:to which account number you want to transfer the amount:").strip()
    transfer=False
    updated_lines=[]
    try:
        with open("accounts.txt", "r") as file:
            lines = file.readlines()
        with open("accounts.txt", "w") as file:
         for line in lines:
                data = line.strip().split(",")
                if data[0] == from_acc_no:
                    sender_balance = float(data[2])
                    transfer_amount = amount()
                    # new_balances = balances - transfer_amount
                    if transfer_amount<=sender_balance:
                        sender_new_balance= sender_balance-transfer_amount
                        updated_lines.append(f"{from_acc_no},{data[1]},{sender_new_balance}\n")
                        transfer=True
                        time = datetime.now().strftime("%d-%m-%Y %A %I:%M %p")

                        with open("transactions.txt", "a") as trans_file:
                            trans_file.write(f"from_acc: {from_acc_no}, to_acc: {to_acc_no}, transfer: {transfer_amount}, {sender_new_balance} ,{time}\n")
                        print(f"money transfer is successful and your New balance: {sender_new_balance}")
                    else:
                        print("not sufficient balance for transfer")
                        updated_lines.append(line)

                elif data[1] == to_acc_no:   
                    receiver_balance = float(data[2])
                    receiver_new_balance=receiver_balance+transfer_amount
                    updated_lines.append(f"{data[0]},{from_acc_no},{receiver_new_balance}\n")
                else:
                    updated_lines.append(line)
        with open ("accounts.txt","w") as file:
            file.writelines(updated_lines)
        if not transfer:
            print(" one or bath Account number/s  not found.")

    except FileNotFoundError:
        print("accounts.txt :file not found.")
    print("-------------------------------------------------------------------------------------")

################################################################################################################
def transaction_history():
    account_number = input("Enter your account number to see you history: ").strip()
    found=False
    try:
        with open("transactions.txt", "r") as transaction_file:
            print(f"{'account_number':<10}{'current balance':<15}{'deposite/withdrawel':<10}{'amount':<15}{'time':}\n")
            for line in transaction_file:
                transaction_data = line.strip().split(',')
                if account_number == transaction_data[0] and len(transaction_data)>=5:
                    print(f"{transaction_data[0]:<10}{transaction_data[1]:<15}{transaction_data[2]:<10}{transaction_data[3]:<15}{transaction_data[4]}\n")
                    found=True
        if not found:
            print("no transaction found for this account")
    except FileNotFoundError:
        print("Transaction file not found ")
#######################################################################################################
def banking_app():
    while True:
        try:
            print("welcome to our banking system----------\n1:Admin\n2:Customer\n3:Exit")
            choice=int(input_validation("enter the option you choose(1-3):"))
            print("\n")
            if choice==1:
                admin_login()
            elif choice==2:
                customer_login()
            elif choice==3:
                print("-----THANKYOU-----")
                break
            else:
                print("Enter the choice between(1-3)")
        except ValueError:
            print(" your option is invalid")
banking_app()
        





