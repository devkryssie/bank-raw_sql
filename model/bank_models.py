from pydantic import BaseModel
from typing import Optional

class BankAccountCreate(BaseModel):
    user_id: int
    initial_balance: Optional[float] = 0.0

class BankAccountResponse(BaseModel):
    id: int
    user_id: int
    balance: float

    class Config:
        from_attributes = True

class TransactionRequest(BaseModel):
    user_id: int
    amount: float

class TransferRequest(BaseModel):
    from_user_id: int
    to_user_id: int
    amount: float

