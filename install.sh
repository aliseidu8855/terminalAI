#!/bin/bash

echo "Installing TerminalAI CLI..."

# Download latest CLI from your GitHub repo
curl -sL https://raw.githubusercontent.com/aliseidu8855/terminalAI/main/cli.py -o terminalai.py

# Make it executable
chmod +x terminalai.py

# Move to global path
sudo mv terminalai.py /usr/local/bin/terminalai

# Create systemd service file
SERVICE_PATH="/etc/systemd/system/terminalai.service"
echo "Creating systemd service..."

sudo tee $SERVICE_PATH > /dev/null <<EOF
[Unit]
Description=TerminalAI Background Service
After=network.target

[Service]
User=$USER
WorkingDirectory=/usr/local/bin
ExecStart=/usr/bin/python3 /usr/local/bin/terminalai optimize
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# Reload daemon and enable service
sudo systemctl daemon-reexec
sudo systemctl enable terminalai
sudo systemctl start terminalai

echo "TerminalAI installed and running!"
echo "You can now run commands like:"
echo "   terminalai translate 'list files modified yesterday'"
echo "   terminalai explain 'sudo apt purge firefox'"
echo "   terminalai optimize"
