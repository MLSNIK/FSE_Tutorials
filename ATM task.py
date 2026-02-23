from decimal import Decimal

accounts = {int(1111):{'name':"Carl", 'pin':int(1234), 'balance':Decimal(500.00), 'blocked': False}, 
            int(1112):{'name':"Jeff", 'pin':int(4343), 'balance':Decimal(7000.00), 'blocked': False}, 
            int(1113):{'name':"Melissa", 'pin':int(1296), 'balance':Decimal(3000.00), 'blocked': False}}

def balance(card_number_balance):
    print (f"\nYour current balance is R{accounts[card_number_balance]['balance']}.\n ")


def withdrawal(card_number_withdrawal):
    amount_to_withdraw = int(input("\n Please enter the amount you wish to withdraw: R"))
    if amount_to_withdraw > accounts[card_number_withdrawal]['balance']:
        print("\nInsufficient funds!\n ")
    else:
        accounts[card_number_withdrawal]['balance'] -= amount_to_withdraw
        print(f"\nWithdrawal of R{amount_to_withdraw} was successful.\n Please remember to take your cash and receipt.\n ")


def deposit(card_number_deposit):
    amount_to_deposit = int(input("\nPlease enter the amount you wish to deposit: R"))
    accounts[card_number_deposit]['balance'] += amount_to_deposit
    print(f"\nDeposit of R{amount_to_deposit} was successful.\n Please remember to take your receipt.\n ")

while True:   
    card_num = int(input("Welcome, please enter your card number: "))

    if card_num in accounts and accounts[card_num]['blocked'] == False:
        pin_attempts_left = 3 
        

        while pin_attempts_left > 0:
            pin = int(input("\nPlease enter your pin: "))

            if pin == accounts[card_num]['pin']:
                while True:
                    menu = int(input(f"\n Hello {accounts[card_num]['name']}!\n === ATM MENU === \n What can we help you with today?\n 1 - View Balance\n 2 - Make a withdrawal \n 3 - Make a deposit\n 4 - Exit\n Please enter your choice: "))

                    if menu == 1:
                        balance(card_num)
                    if menu == 2: 
                        withdrawal(card_num)
                    if menu == 3:
                        deposit(card_num)
                    if menu == 4:
                        print("Your session has ended. Thank you! Have a wonderful day!")
                        exit()
                break  
            else: 
                pin_attempts_left -= 1
                if pin_attempts_left > 0:
                    print(f"\nIncorrect PIN entered. You have {pin_attempts_left} attempts left.\n ")
                else:
                    accounts[card_num]['blocked'] = True
                    print("\nMaximum attempts exceeded. For the account holders protection, this card has been frozen. Please contact your nearest branch. Good bye!\n ")
                    exit()

    elif card_num in accounts and accounts[card_num]['blocked'] == True:
        print("\nThis card has been blocked for the account holder's protection. Please contact your neartest branch.\n ") 
        exit()    
    else:
        print("\nYou have entered an incorrect card number.\n ")