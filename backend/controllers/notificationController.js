import { buildCopilotContext } from "../services/contextBuilder.js";
import { callNotificationAI } from "../services/aiService.js";

export async function generateNotification(req, res) {
  try {
    const context = buildCopilotContext();

    const aiResponse = await callNotificationAI(context);

    res.json(aiResponse);
  } catch (error) {
    console.error("Notification error:", error.message);
    res.status(500).json({ error: "Failed to generate notification" });
  }
}
export default { generateNotification };
