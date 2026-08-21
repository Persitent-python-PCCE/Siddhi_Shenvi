accounts = {
    "ACC-1001": 5000.0,
    "ACC-1002": 250.0,
    "ACC-1003": 0.0
}


class InsufficientFundsError(Exception):
    pass

class InvalidAmountError(ValueError):
    pass

def withdraw(account_id, amount):
    if account_id not in accounts:
        raise KeyError(account_id)

    if amount <= 0:
        raise InvalidAmountError()

    if amount > accounts[account_id]:
        raise InsufficientFundsError()

    accounts[account_id] -= amount
    return accounts[account_id]


def process_withdrawal(account_id, amount):

    try:
        balance = withdraw(account_id, amount)
        print(f"Withdrawal successful. New Balance: {balance}")

    except KeyError:
        print(f"Unknown account: {account_id}")

    except InvalidAmountError:
        print("Withdrawal amount must be positive.")

    except InsufficientFundsError:
        print(f"Insufficient funds in {account_id}.")


# ---------------- Test Cases ----------------

process_withdrawal("ACC-1001", 1200)
process_withdrawal("ACC-9999", 100)
process_withdrawal("ACC-1002", -50)
process_withdrawal("ACC-1003", 100),