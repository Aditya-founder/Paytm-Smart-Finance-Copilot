import axios from "axios";

const AI_BASE_URL = "http://localhost:8000";

export async function callCopilotAI(context, question) {
  const response = await axios.post(`${AI_BASE_URL}/copilot/ask`, {
    context,
    question,
  });
  return response.data;
}

export async function callReminderAI(context) {
  const response = await axios.post(`${AI_BASE_URL}/reminder/generate`, {
    context,
  });
  return response.data;
}

export async function callNotificationAI(context) {
  const response = await axios.post(`${AI_BASE_URL}/notification/generate`, {
    context,
  });
  return response.data;
}

export default { callCopilotAI, callReminderAI, callNotificationAI };
