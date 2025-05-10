def option():
    global option
    while True:
        try:
            option=int(input("enter the option you choose:"))
            break
        except ValueError:
            print(" your choosed option is invalid")
#==staff menu==================================================================
def staff_menu():
    print("===============MENU OPTION===============")
    print("1:adding new customer and account creation")
    print("2:Deposits")
    print("3:Withdrawels")
    print("4:Check balances")
    print("5:Transaction between accounts")
    print("6:Transaction history")
    print("7:update the customer")
    print("8:exit")
    option()
    if choice == "1":
        user_details_input()
        new_account_creation()
    elif choice == "2":
        deposits()
    elif choice == "3":
        withdrawel()
    elif choice == "4":
        balance_check()
    elif choice == "5":
        transfer_between_accounts()   
    elif choice == "6":
        transaction_history()
    elif choice == "7":
        update_customer()
    else :
        print('thank you for using our banking sercices')
#===customer menu=======================================================================
def  customer_menu():
    print("===============MENU OPTION===============")
    print("1:Deposit")
    print("2:Withdrawel")
    print("3:Check balance")
    print("4:Transfer between accounts")
    print("5:Transaction history")
    print("6:Check balances")
    print("7:Exit")
    option()
    if choice == "1":
        deposits()
    elif choice == "2":
        withdrawel()
    elif choice == "3":
        balance_check()
    elif choice == "4":
        transfer_between_accounts()   
    elif choice == "5":
        transaction_history()
    elif choice == "6":
        balance_check()
    else :
        print('thank you for using our banking sercices')
#====NEW CUSTOMER CREATION===============================================
def user_details_input():
    print ("-------------------------------")
    print ("  CUSTOMER INFORMATION INPUT    ")
    print ("-------------------------------")
    username= input("enter the name:")
    address=input("enter the address:")
    nic=input("enter the nic number :")
    phone_number=input("enter the phone number:")
    password=input("enter the password:")
    with open ("users.txt","a")as file:
        file.write(f"{username},{password}\n")
        file.write("-------------------------------------------------------------------------\n")
    with open("customer_details.txt","a")as file:
        file.write(f"username:{username}\npassword:{password}\nNIC:{nic}\naddress:{address}\nphone number:{phone_number}\n")
        file.write("-----------------------------------------------------------------------------\n")
    print('SUCCESSFULLY CREATE AN ACCOUNT ')
    print("==================================================================================================")
    return[username,password,nic,address,phone_number]
#===NEW CUSTOMER ACCOUNT CREATION=========================================
customer_details=user_details_input()
def new_account_creation():
    global is_customer
    if is_customer==2:
        account_number=(f"ACC{int(customer_details[2])+987654321012}UIC")
    while True:
        try:
            balance=int(input("Enter the initial amount to create an account:"))
            if balance>100:#initial balance must be greater than 100
                break
            else:
                print("initial balance must be greater than 100")
        except ValueError:
            print('ENTER A VALID AMOUNT')
    with open ("accounts.txt","a")as file:
        file.write(f"{account_number},{customer_details[0]},{balance},\n")
    print(f"Account created successfully! The account Number is: {account_number}")
#===ACCOUNT DETAILS========================================================
def Account_details():
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
        print("-----------------------------------------------------------------------\n")
                user_found=True
    if user_found!= True:
        print("please enter a user name")
#====DEPOSIT AND WITHDRAWEL=================================================
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
#deposit------------------------------------------------------------------------------
def deposits():
    depo=False
    account_no=input("enter the account number:").strip()
    with open("accounts.txt","r")as file:
        lines = file.readlines()
    with open("accounts.txt","a")as file:
        for line in lines:
            data=line.strip().split(",")
            if data[0]==account_no:
                deposite_amount=amount()
                balances=float(data[2])
                new_balances=(balances + deposite_amount)
                file.write(f"{account_no},{data[1]},{new_balances}")
                depo=True
                time = datetime.now().strftime("%d-%m-%Y %A %I %M %p")
                with open("Transactions.txt","a") as file:
                    file.write(f"{account_no},{balances},deposit,{new_balances},{time}\n")
                print(f"deposite successful:) and your new balance is{new_balances}")
            else:
                file.write(line)
        if depo!=True:
            print("Account not found")
#WITHDRAWEL------------------------------------------------------------------------------------------------





