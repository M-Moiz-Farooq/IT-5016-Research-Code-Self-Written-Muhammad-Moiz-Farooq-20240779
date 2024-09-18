class BankSystem:
    accountid = 1000
    totalaccounts = 0
    totalbalance = 0
    accounts = []

    def __init__(self):
        self.status = True

    def create_account(self):
        name = input("Please enter your name: ")
        address = input("Please enter your address: ")
        phone = input("Please enter your phone number: ")
        initial_balance = float(input("Please enter the initial balance: "))
        BankSystem.accountid += 1
        self.accountid = BankSystem.accountid
        account_number = str(BankSystem.accountid)[-4:]
        return {
            "name": name,
            "address": address,
            "phone": phone,
            "balance": initial_balance,
            "account_number": account_number
        }

    def submit_money(self, account_number):
        amount = float(input("Please enter the amount to submit: "))
        for account in self.accounts:
            if account["account_number"] == account_number:
                account["balance"] += amount
                BankSystem.totalbalance += amount
                print(f"Amount submitted successfully. New balance: ${account['balance']}")
                return
        print("Account not found.")

    def withdraw_money(self, account_number):
        amount = float(input("Please enter the amount to withdraw: "))
        for account in self.accounts:
            if account["account_number"] == account_number:
                if account["balance"] >= amount:
                    account["balance"] -= amount
                    BankSystem.totalbalance -= amount
                    print(f"Amount withdrawn successfully. New balance: ${account['balance']}")
                    return
                else:
                    print("Insufficient balance.")
                    return
        print("Account not found.")

    def delete_account(self, account_number):
        for account in self.accounts:
            if account["account_number"] == account_number:
                self.accounts.remove(account)
                BankSystem.totalaccounts -= 1
                BankSystem.totalbalance -= account["balance"]
                print("Account deleted successfully.")
                return
        print("Account not found.")

    def transfer_money(self, sender_account_number, receiver_account_number):
        amount = float(input("Please enter the amount to transfer: "))
        for sender_account in self.accounts:
            if sender_account["account_number"] == sender_account_number:
                for receiver_account in self.accounts:
                    if receiver_account["account_number"] == receiver_account_number:
                        if sender_account["balance"] >= amount:
                            sender_account["balance"] -= amount
                            receiver_account["balance"] += amount
                            BankSystem.totalbalance -= amount
                            BankSystem.totalbalance += amount
                            print(f"Amount transferred successfully. Sender's new balance: ${sender_account['balance']}. Receiver's new balance: ${receiver_account['balance']}")
                            return
                        else:
                            print("Insufficient balance.")
                            return
                print("Receiver account not found.")
                return
        print("Sender account not found.")

    def display_account(self, account_number):
        for account in self.accounts:
            if account["account_number"] == account_number:
                print(f"Account Number: {account['account_number']}")
                print(f"Name: {account['name']}")
                print(f"Address: {account['address']}")
                print(f"Phone: {account['phone']}")
                print(f"Balance: ${account['balance']}")
                return
        print("Account not found.")

    def display_statistics(self):
        print(f"Total accounts: {BankSystem.totalaccounts}")
        print(f"Total balance: ${BankSystem.totalbalance}")


def main():
    system = BankSystem()
    print("========================================")
    print("   Welcome to the bank system")
    print("========================================")
    while True:
        choice = input("\n1. Create Account\n2. Submit Money\n3. Withdraw Money\n4. Delete Account\n5. Transfer Money\n6. Display Account\n7. Display Statistics\n8. Exit\nChoose an option: ")
        if choice == "1":
            account = system.create_account()
            system.accounts.append(account)
            BankSystem.totalaccounts += 1
            BankSystem.totalbalance += account["balance"]
            print(f"Account created successfully. Account number: {account['account_number']}")

        elif choice == "2":
            account_number = input("Please enter the account number: ")
            system.submit_money(account_number)

        elif choice == "3":
            account_number = input("Please enter the account number: ")
            system.withdraw_money(account_number)

        elif choice == "4":
            account_number = input("Please enter the account number: ")
            system.delete_account(account_number)

        elif choice == "5":
            sender_account_number = input("Please enter the sender's account number: ")
            receiver_account_number = input("Please enter the receiver's account number: ")
            system.transfer_money(sender_account_number, receiver_account_number)

        elif choice == "6":
            account_number = input("Please enter the account number: ")
            system.display_account(account_number)

        elif choice == "7":
            system.display_statistics()

        elif choice == "8":
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()