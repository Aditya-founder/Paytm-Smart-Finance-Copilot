from pydantic import BaseModel
from typing import Dict, Any, Optional


class CopilotRequest(BaseModel):
    context: Dict[str, Any]
    question: str


class ReminderRequest(BaseModel):
    context: Dict[str, Any]


class NotificationRequest(BaseModel):
    context: Dict[str, Any]


class AIResponse(BaseModel):
    type: Optional[str]
    message: Optional[str]
    insight: Optional[str]
    reason: Optional[str]
    recommended_action: Optional[str]
    priority: Optional[str]
