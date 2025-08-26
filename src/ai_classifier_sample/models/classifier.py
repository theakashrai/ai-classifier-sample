from pydantic import BaseModel, Field


class ClassifierOutput(BaseModel):
    message: str = Field(..., description="The original message that was classified")
    category: str = Field(..., description="The category of the message: 'Support, Feedback, Complaint', 'Order Tracking', 'Refund/Exchange'")