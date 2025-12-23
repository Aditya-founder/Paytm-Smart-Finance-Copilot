from fastapi import FastAPI
from ai_service.models.schemas import (
    CopilotRequest,
    ReminderRequest,
    NotificationRequest
)


from ai_service.services.copilot_service import generate_copilot_response
from ai_service.services.reminder_service import generate_payment_reminder
from ai_service.services.notification_service import generate_notification

app = FastAPI(title="Paytm Personalized AI Service")


@app.post("/copilot/ask")
def copilot(req: CopilotRequest):
    return generate_copilot_response(req.context, req.question)


@app.post("/reminder/generate")
def reminder(req: ReminderRequest):
    return generate_payment_reminder(req.context)


@app.post("/notification/generate")
def notification(req: NotificationRequest):
    return generate_notification(req.context)
