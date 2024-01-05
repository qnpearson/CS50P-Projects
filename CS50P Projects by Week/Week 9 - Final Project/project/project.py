#Title: QP Bank (Prototype Banking Application)
#Quinn Pearson from New York, NY (United States)

import sys
import random as r
from rich.console import Console
from rich.table import Table
import pandas as pd

#Make a Banking Program

#Create an Account [1]
#Access Their Account Information [2]
#Make Deposits
#Make Withdrawls
#(Transfers)
#Close their Account
#Quit System
#Display System Information

#Accounts Require:
#Name
#Pin (Password)
#Account Number
#Routing Number

column_head = ["Name", "Balance", "Pin", "Account Number", "Routing Number"]
customers = pd.DataFrame(columns=column_head)

def main():
    customers = pd.DataFrame(columns=column_head)
    while True:
        table()
        choice = input("Input option number: ")
        print(choice)
        match choice:
            case "1":
                name = input("To create an account please input your name. (First Last) ").lower()
                pin = input("Please input a 4-digit pin. ")
                customer = create_account(name, pin)
                customers = pd.concat([customers, customer], ignore_index=True)
                #print(customers)
            case "2":
                result = access_account(customers)
                print(result)
            case "3":
                name = input("Please input your name. (First Last) ").lower()
                pin = input("Please input your 4-digit pin. ")
                deposit = input("How much money would you like to deposit? $")
                result = make_deposit(customers, name, pin, deposit)
                print(result)
            case "4":
                name = input("Please input your name. (First Last) ").lower()
                pin = input("Please input your 4-digit pin. ")
                withdrawal = input("How much money would you like to withdraw? $")
                result = make_withdrawal(customers, name, pin, withdrawal)
                print(result)
            case "5":
                name = input("Please input your name. (First Last) ").lower()
                pin = input("Please input your 4-digit pin. ")
                transfer = input("How much money would you like to transfer? $")
                routing_number = input("Please enter the routing number of the account you would like to transfer to. ")
                result = make_transfer(customers, name, pin, transfer, routing_number)
                print(result)
            case "6":
                i = close_account(customers)
                customers = customers.drop(i)
            case "7":
                password = input("Please enter adminastrative password. ")
                if password == "CS50":
                    print(customers)
                else:
                    print("Invalid password.")
            case "8":
                sys.exit("Quitting system...")
            case _:
                sys.exit("Invalid choice. Please try again.")


def table():
    bank_table = Table(title = "Welcome to QP Bank. Select an option number.")
    bank_table.add_column("Number", justify = "center", style = "cyan", no_wrap =True)
    bank_table.add_column("Option", justify = "left", style = "magenta", no_wrap =True)
    bank_table.add_row("[1]", "Create an account.")
    bank_table.add_row("[2]", "Access your account information.")
    bank_table.add_row("[3]", "Make a deposit.")
    bank_table.add_row("[4]", "Make a withdrawal.")
    bank_table.add_row("[5]", "Make a transfer.")
    bank_table.add_row("[6]", "Close an account.")
    bank_table.add_row("[7]", "Administrative view.")
    bank_table.add_row("[8]", "Quit system.")
    console = Console()
    console.print(bank_table)

def create_account(name, pin):
    account_num = r.randint(100000, 999999) #6 Digits
    routing_num = r.randint(10000, 99999) #5 Digits
    new_account = pd.DataFrame({"Name" : name, "Balance" : int(0), "Pin" : pin, "Account Number" : account_num, "Routing Number": routing_num,}, index = [0])
    new = pd.concat([new_account, customers.loc[:]]).reset_index(drop=True)
    return new

def access_account(customers):
    name = input("Please input your name. (First Last) ").lower()
    pin = input("Please input your 4-digit pin. ")
    local_customer = customers[customers["Name"] == name]
    truth = local_customer["Pin"] == pin
    if (str(truth.values)).count("True") == 1:
        print(f"Hello {name}, here is your account information.")
        return(customers[(customers["Pin"] == pin) & (customers["Name"] == name)])
    else:
        return("Invalid name or pin. Please try again.")

def make_deposit(customers, name, pin, deposit):
    local_customer = customers[customers["Name"] == name]
    truth = local_customer["Pin"] == pin
    if (str(truth.values)).count("True") == 1:
        print(f"Hello {name}, here is your account information.")
        print(customers[(customers["Pin"] == pin) & (customers["Name"] == name)])
        try:
            deposit = int(deposit)
            if deposit >= 0:
                for i in customers[(customers["Pin"] == pin) & (customers["Name"] == name)].index:
                    customers.at[i, "Balance"] += deposit
                    return(f"Updated Balance: ${customers.at[i, 'Balance']}")
            else:
                return("Invalid amount. Can only deposit positive dollars. Try again.")
        except ValueError:
           return("Invalid amount. Please only use whole dollars and try again.")
    else:
        return("Invalid name or pin. Please try again.")

def make_withdrawal(customers, name, pin, withdrawal):
    local_customer = customers[customers["Name"] == name]
    truth = local_customer["Pin"] == pin
    if (str(truth.values)).count("True") == 1:
        print(f"Hello {name}, here is your account information.")
        print(customers[(customers["Pin"] == pin) & (customers["Name"] == name)])
        try:
            withdrawal = int(withdrawal)
            if withdrawal >= 0:
                for i in customers[(customers["Pin"] == pin) & (customers["Name"] == name)].index:
                    if int(customers.at[i, "Balance"]) >= withdrawal:
                        customers.at[i, "Balance"] -= withdrawal
                        return(f"Updated Balance: ${customers.at[i, 'Balance']}")
                    else:
                        return("Withdrawal exceeds available balance. Please try again.")
            else:
                return("Invalid amount. Can only withdraw positive dollars. Try again.")
        except ValueError:
            return("Invalid amount. Please only use whole dollars and try again.")
    else:
        return("Invalid name or pin. Please try again.")

def make_transfer(customers, name, pin, transfer, routing_number):
    local_customer = customers[customers["Name"] == name]
    truth = local_customer["Pin"] == pin
    print(local_customer)
    print(truth)
    if (str(truth.values)).count("True") == 1:
        print(f"Hello {name}, here is your account information.")
        print(customers[(customers["Pin"] == pin) & (customers["Name"] == name)])
        try:
            transfer = int(transfer)
            routing_number = int(routing_number)
            if transfer >= 0:
                for i in customers[(customers["Pin"] == pin) & (customers["Name"] == name)].index:
                    if int(customers.at[i, "Balance"]) >= transfer:
                        try:
                            for x in customers[(customers["Routing Number"] == routing_number)].index:
                                customers.at[i, "Balance"] -= transfer
                                customers.at[x, "Balance"] += transfer
                                return(f"Transfer Completed Successfully. Updated Balance: ${customers.at[i, 'Balance']}")
                        except:
                            return("Transfer unsuccessful. Please try again.")
                    else:
                        return("Transfer exceeds available balance. Please try again.")
            else:
                return("Invalid amount. Can only transfer positive dollars. Try again.")
        except ValueError:
            return("Invalid amount. Please only use whole dollars and try again.")
    else:
        return("Invalid name or pin. Please try again.")

def close_account(customers):
    name = input("Please input your name. (First Last)").lower()
    pin = input("Please input your 4-digit pin. ")
    local_customer = customers[customers["Name"] == name]
    truth = local_customer["Pin"] == pin
    if (str(truth.values)).count("True") == 1:
        print(f"Hello {name}, here is your account information.")
        print(customers[(customers["Pin"] == pin) & (customers["Name"] == name)])
        sure = input("Are you sure you would like to close your account? (Yes/No) ").lower()
        if sure == "yes":
            for i in customers[(customers["Pin"] == pin) & (customers["Name"] == name)].index:
                print(f"Account closed. Here is the remaining balanced returned ${customers.at[i, 'Balance']}. Thank you for banking with us and we hope to see you again.")
                return i
        elif sure == "no":
            print("Returning to home screen.")
        else:
            print('Invalid response. Please try again and type "Yes" or "No".')
    else:
        print("Invalid name or pin. Please try again.")

if __name__ == "__main__":
    main()