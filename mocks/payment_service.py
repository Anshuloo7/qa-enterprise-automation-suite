from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PaymentRequest(BaseModel):
    amount: float
    currency: str

@app.post("/process-payment")
def process_payment(payment: PaymentRequest):
    if payment.amount > 0:
        return {"status": "success", "message": "Payment processed successfully"}
    else:
        return {"status": "failed", "message": "Invalid amount"}
