import { buildReminderContext } from "../services/contextBuilder.js";
import { callReminderAI } from "../services/aiService.js";

export async function generateReminder(req, res) {
  const { upcomingPayment } = req.body;

  const context = buildReminderContext(upcomingPayment);
  const aiResponse = await callReminderAI(context);

  res.json(aiResponse);
}
export default { generateReminder };
