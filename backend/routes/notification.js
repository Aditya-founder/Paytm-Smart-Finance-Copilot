import express from "express";
import { generateNotification } from "../controllers/notificationController.js";

const router = express.Router();

router.post("/generate", generateNotification);

export default router;
