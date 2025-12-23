import express from "express";
import { generateReminder } from "../controllers/reminderController.js";

const router = express.Router();
router.post("/generate", generateReminder);

export default router;
