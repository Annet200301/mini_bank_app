from datetime import datetime
#==staff menu==================================================================
def staff_menu():
    global is_customer
    print("===============MENU OPTION===============")
    print("1:adding new customer and account creation")
    print("2:Deposits")
    print("3:Withdrawals")
    print("4:Check balances")
    print("5:Transaction between accounts")
    print("6:Transaction history")
    print("7:update the customer")
    print("8:exit")
    while True:
        try:
            choice =int(input("enter the option you choose:"))
            break
        except ValueError:
            print(" your chosen option is invalid")

    if choice == 1:
        is_customer=2
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
    elif choice == 7:
        update_customer()
    else :
        print('thank you for using our banking sercices')
#===customer menu=======================================================================
def  customer_menu():
    print("===============MENU OPTION===============")
    print("1:Deposit")
    print("2:Withdrawal")
    print("3:Check balance")
    print("4:Transfer between accounts")
    print("5:Transaction history")
    print("6:Check balances")
    print("7:Exit")
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
    elif choice == 6:
        balance_check()
    else :
        print('thank you for using our banking sercices')
#---------------------------------------------Login -----------------------------------------  
def customer_login():
    while True:
        username = input("Enter your username:").strip()
        password = input('Enter your password:').strip()
        login_sucessful=False
        try :
            with open ("user.txt","r") as User_file:
                for lines in User_file:
                    users=line.strip().split(",")
                    if len(users)==2 and users[0]==username and users[1]==password:
                        print("-----LOGIN SUCCESSFUL-----")
                        customer_menu()
                        login_successful=True
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
        username = input("Enter your username:").strip()
        password = input('Enter your password:').strip()
        if username==admin_id and password==admin_password:
                print("-----LOGIN SUCCESSFUL-----")
                staff_menu()
        else:
            print("username or password is wrong!")                
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
        username= input("enter the name:").strip()
        if username in check_user_name:
            print ('oops!!  user name already exist try a new one ')
        else:
            break
    address=input("enter the address:")
    nic=input("enter the nic number :")
    phone_number=input("enter the phone number:")
    password=input("enter the password:")


    with open ("users.txt","a")as file:
        file.write(f"{username},{password}\n")

    with open("customer_details.txt","a")as file:
        file.write(f"username:{username}\npassword:{password}\nNIC:{nic}\naddress:{address}\nphone number:{phone_number}\n")
        file.write("-----------------------------------------------------------------------------\n")
    print('SUCCESSFULLY CREATED   &   SAVED THE CUSTOMER DETAILS :) ')
    print("==================================================================================================")
    return[username, password, nic, address, phone_number]
#------------------------------------------------------------------------------------------------------------------------------
#                      NEW ACCOUNT CREATION
#------------------------------------------------------------------------------------------------------------------------------
def new_account_creation():
    global is_customer
    global customer_details
    customer_details=user_details_input()
    if is_customer==2: 
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

    print(f"Account created successfully! The account Number is: {account_number}")

#BALANCE CHECK ##################################################################################################
def balance_check():
    print("------------------------------------------------------------------------------------------------")
    print("                              ACCOUNT DETAILS                                                   ")
    print("------------------------------------------------------------------------------------------------")

    username=input ("Enter the user name:").strip()
    user_found=False
    with open ("accounts.txt","r")as file:
        for line in file:
            data=line.strip().split(",")
            if data[1]==username :
                print(f"{data[1]}:-:= Account numbers:-{(data[0])}\t,balance is:-{data[2]}\n")
                user_found=True
    print("-----------------------------------------------------------------------\n")
                
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
#--------------------------------------------------------------------------------------------------------------------
def withdrawal():
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
#TRANSFER BETWEEN ACCOUNTS########################################################################################
def transfer_between_accounts():
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

                        with open("transaction.txt", "a") as trans_file:
                            trans_file.write(f"from_acc: {from_acc_no}, to_acc: {to_acc_no}, transfer: {transfer_amount}, {new_balances} ,{time}\n")
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

################################################################################################################
def transaction_history():
    account_number = input("Enter your account number to see you history: ").strip()
    try:
        with open("transactions.txt", "r") as transaction_file:
            print(f"{'account_number':<10}{'current balance':<10}{'deposite/withdrawel':<10}{'amount':<10}{'time':}\n")
            for line in transaction_file:
                transaction_data = line.strip().split(',')
                if account_number == transaction_data[0]:
                    print(f"{transaction_data[0]:<10}{transaction_data[1]:<15}{transaction_data[2]:<10}{transaction_data[3]:<15}{transaction_data[4]}\n")
                else:
                    continue
    except FileNotFoundError:
        print("Transaction file not found :(") 
################################################################################################################
def update_customer():
    username=input("Enter the user name")
    is_customer= False
    updated_lines=[]
    try:
        with open("customer_details.txt", "r") as file:
            lines = file.readlines()

        
        for line in lines:
            data = line.strip().split(",")
            if data[0] == username:
                is_customer = True
                print(" ------------options to choose\n----------1:username\n2:password\n3:nic\n4:Address\n5:phone nuumber")
                while True:
                    try:
                        option = int(input("Enter data to update(1-5):"))
                        break
                    except ValueError:
                            print("ENTER A VALID OPTION!")
                if option == 1:
                    new_username = input("enter the new username: ").strip()
                    data[0]=new_username
                    try:
                        with open ("users.txt","r") as file:
                            for line in file:
                                if "," in line:
                                    check_user_name.add(line.strip().split()[0])
                    except FileNotFoundError:
                        pass
                    while True:
                        username= input("enter the name:").strip()
                        if username in check_user_name:
                            print ('oops!!  user name already exist ')
                            print ('enter a new one with any changes')
                        else:
                            break
                elif option==2:
                    new_password=input("Enter the new password:")
                    data[1]=new_password
                elif option == 3:
                    new_nic = input("enter the new nic: ")
                    data[2]=new_nic
                elif option== 4:
                    new_address = input("enter the new address: ")
                    data[3]=new_address
                elif option == 5:
                    new_number = input("enter the new phone number: ")
                    data[4]=new_number

                updated_lines.append(",".join(data) + "\n")
            else:
                updated_lines.append(line)
        with open("customer_details.txt","w")as file:
            file.writelines(updated_lines)

        if is_customer:
            print("successfully updated the customer")
        else:
            print("user name not found")

    except FileNotFoundError:
        print("customer_details.txt  file not found.")  
#######################################################################################################
def banking_app():
    while True:
        print("welcome to our banking system----------\n1:Admin\n2:Customer\n3:Exit")
        while True:
            try:
                choice=int(input("enter the option you choose(1-3):"))
                break
            except ValueError:
                print(" your option is invalid")
        if choice==1:
            admin_login()
        elif choice==2:
            customer_login()
        elif choice==3:
            print("-----THANKYOU-----")
            break
        else:
            print("Enter the choice between(1-3)")
banking_app()
        





