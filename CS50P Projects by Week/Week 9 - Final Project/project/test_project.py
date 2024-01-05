from project import create_account, make_deposit, make_withdrawal, make_transfer, close_account
import pytest
import pandas as pd

column_head = ["Name", "Balance", "Pin", "Account Number", "Routing Number"]
customers = pd.DataFrame(columns=column_head)

customer1 = create_account(name = "David Malan", pin = "5050")
customer2 = create_account(name = "Quinn", pin = "1234")
customers = pd.concat([customers, customer1, customer2], ignore_index=True)

def mini():
    for i in customers[(customers["Name"] == "Quinn")].index:
        return customers.at[i, "Routing Number"]

mini_routing_number = mini()

def main():
    test_make_deposit()
    test_make_withdrawal()
    test_make_transfer()
    print(pytest.ExitCode)

def test_make_deposit():
    assert(make_deposit(customers, name = "David Malan", pin = "5050", deposit = "50")) == "Updated Balance: $50"
    assert(make_deposit(customers, name = "David Malan", pin = "5050", deposit = "50.00")) == "Invalid amount. Please only use whole dollars and try again."

def test_make_withdrawal():
    assert(make_withdrawal(customers, name = "David Malan", pin = "5050", withdrawal = "25")) == "Updated Balance: $25"
    assert(make_withdrawal(customers, name = "David Malan", pin = "5050", withdrawal = "100")) == "Withdrawal exceeds available balance. Please try again."

def test_make_transfer():
    assert(make_transfer(customers, name = "David Malan", pin = "5050", transfer = "25", routing_number = mini_routing_number)) == "Transfer Completed Successfully. Updated Balance: $0"
    assert(make_transfer(customers, name = "David Malan", pin = "5050", transfer = "25", routing_number = mini_routing_number)) == "Transfer exceeds available balance. Please try again."

if __name__ == "__main__":
    main()