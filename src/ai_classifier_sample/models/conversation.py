from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ConversationTurn(BaseModel):
    message: str = Field(..., description="The message content")
    speaker: str = Field(..., description="Who sent the message: 'user' or 'agent'")
    timestamp: datetime = Field(default_factory=datetime.now)
    intent: Optional[str] = Field(None, description="Classified intent for this turn")


class ConversationalClassifierOutput(BaseModel):
    message: str = Field(..., description="The current message being classified")
    reasoning: str = Field(..., description="Reasoning for the classification")
    intent_transition: str = Field(..., description="Whether this is CONTINUE, NEW, or CLARIFICATION")
    intent: str = Field(..., description="The classified intent")
    confidence: str = Field(..., description="Confidence level: HIGH, MEDIUM, LOW")