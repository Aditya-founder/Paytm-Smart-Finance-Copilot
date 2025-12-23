import express from "express";
import cors from "cors";

import copilotRoutes from "./routes/copilot.js";
import reminderRoutes from "./routes/reminder.js";
import notificationRoutes from "./routes/notification.js";

const app = express();
app.use(cors());
app.use(express.json());

app.use("/copilot", copilotRoutes);
app.use("/reminder", reminderRoutes);
app.use("/notification", notificationRoutes);

app.get("/health", (req, res) => {
  res.json({ status: "Backend running" });
});

app.listen(5000, () => {
  console.log("Backend running on port 5000");
});
export default app;
