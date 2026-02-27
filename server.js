import express from "express";
import fetch from "node-fetch";
import dotenv from "dotenv";
import path from "path";
import { fileURLToPath } from "url";

dotenv.config();

const app = express();
app.use(express.json());

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Serve frontend
app.use(express.static(path.join(__dirname, "public")));

app.post("/chat", async (req, res) => {
  const userMessage = req.body.message;

  if (!userMessage) {
    return res.json({ reply: "Please type something." });
  }

  try {
    const response = await fetch(
      "https://api.groq.com/openai/v1/chat/completions",
      {
        method: "POST",
        headers: {
          "Authorization": `Bearer ${process.env.GROQ_API_KEY}`,
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          model: "llama-3.1-8b-instant",
          messages: [
            { role: "user", content: userMessage }
          ]
        })
      }
    );

    const data = await response.json();

    if (data.error) {
      return res.json({ reply: "Groq Error: " + data.error.message });
    }

    res.json({
      reply: data.choices[0].message.content
    });

  } catch (error) {
    res.json({ reply: "AI Connection Error" });
  }
});

app.listen(3000, () => {
  console.log("Server running at http://localhost:3000");
});