#!/bin/bash

echo "🌐 Setting up TerminalGPT cloud CLI..."

# 🔗 Define your hosted API URL
API_URL="https://terminalgpt.onrender.com"

# 🔐 Prompt for user token
echo "Enter your X-Token (auth key):"
read -r USER_TOKEN

# 📝 Download CLI template
curl -s https://raw.githubusercontent.com/yourusername/terminalgpt/main/cli.py -o terminalgpt.py

# 🧠 Inject API URL and token
sed -i "s|API_URL = .*|API_URL = \"$API_URL\"|" terminalgpt.py
sed -i "s|TOKEN = .*|TOKEN = \"$USER_TOKEN\"|" terminalgpt.py

# 🔗 Make globally accessible
chmod +x terminalgpt.py
sudo mv terminalgpt.py /usr/local/bin/terminalgpt

echo "✅ Installed TerminalGPT CLI globally!"
echo "📟 Try: terminalgpt translate \"show logged-in users\""
