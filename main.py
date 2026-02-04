from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="ATM API")


# ATM class (business logic)
class ATM:
    def __init__(self):
        self.balance = 0.0


atm = ATM()


# Request Models
class Amount(BaseModel):
    amount: float


# Routes

@app.get("/")
def home():
    return {
        "message": "Welcome to ATM API",
        "actions": {
            "deposit": "/deposit",
            "withdraw": "/withdraw",
            "balance": "/balance"
        }
    }


@app.post("/deposit")
def deposit_money(data: Amount):
    if data.amount <= 0:
        return {"error": "Deposit amount must be positive"}

    atm.balance += data.amount
    return {
        "message": "Deposit successful",
        "deposited": data.amount,
        "balance": atm.balance
    }


@app.post("/withdraw")
def withdraw_money(data: Amount):
    if data.amount <= 0:
        return {"error": "Withdrawal amount must be positive"}

    if data.amount > atm.balance:
        return {"error": "Insufficient funds"}

    atm.balance -= data.amount
    return {
        "message": "Withdrawal successful",
        "withdrawn": data.amount,
        "balance": atm.balance
    }


@app.get("/balance")
def balance_inquiry():
    return {
        "balance": atm.balance
    }
