import { buildCopilotContext } from "../services/contextBuilder.js";
import { callCopilotAI } from "../services/aiService.js";

export async function askCopilot(req, res) {
  try {
    const { question } = req.body;
    const context = buildCopilotContext();
    const aiResponse = await callCopilotAI(context, question);
    res.json(aiResponse);
  } catch (err) {
    console.error("Copilot error:", err.message);
    res.status(500).json({ error: "AI service unavailable" });
  }
}

export default { askCopilot };
