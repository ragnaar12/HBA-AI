const express = require('express');
const fetch = require('node-fetch');
const path = require('path');

const app = express();
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public'))); // sert index.html

// 💡 Remplace ici par ta clé API réelle
const OPENAI_API_KEY = "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";

app.post('/api/chat', async (req, res) => {
  const message = req.body.message;

  const response = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${OPENAI_API_KEY}`
    },
    body: JSON.stringify({
      model: 'gpt-3.5-turbo',
      messages: [{ role: 'user', content: message }]
    })
  });

  const data = await response.json();
  res.json({ reply: data.choices[0].message.content });
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`✅ Serveur en ligne sur http://localhost:${port}`);
});


