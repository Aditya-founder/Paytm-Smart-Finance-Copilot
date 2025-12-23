import express from "express";
import { askCopilot } from "../controllers/copilotController.js";

const router = express.Router();
router.post("/ask", askCopilot);

export default router;
