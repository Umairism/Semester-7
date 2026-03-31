#!/bin/bash

# -------------------------------
# VS Code Reset + Copilot Cleanup
# Fedora/Linux
# -------------------------------

echo "Closing all VS Code instances..."
killall code 2>/dev/null

echo "Backing up VS Code settings and extensions..."
mkdir -p ~/vscode_backup
cp -r ~/.config/Code/User ~/vscode_backup/User-backup
cp -r ~/.vscode/extensions ~/vscode_backup/extensions-backup

echo "Clearing cached sessions and Settings Sync..."
rm -rf ~/.config/Code/Cache
rm -rf ~/.config/Code/CachedData
rm -rf ~/.config/Code/User/globalStorage
rm -rf ~/.config/Code/User/globalStorage/state.vscdb*
echo "Cache cleared."

# -------------------------------
# Disable conflicting AI extensions temporarily
# -------------------------------
echo "Disabling potentially conflicting AI extensions..."
code --disable-extension openai.chatgpt
code --disable-extension ms-toolsai.jupyter
code --disable-extension ms-toolsai.jupyter-keymap
code --disable-extension ms-toolsai.vscode-jupyter-cell-tags
code --disable-extension ms-toolsai.vscode-jupyter-slideshow
code --disable-extension ms-toolsai.vscode-jupyter-renderers
code --disable-extension ms-vscode.vscode-speech
echo "Conflicting extensions disabled."

# -------------------------------
# Keep only GitHub Copilot active
# -------------------------------
echo "Ensuring GitHub Copilot is enabled..."
code --enable-extension github.copilot-chat
code --enable-extension github.codespaces
code --enable-extension github.vscode-github-actions
echo "Copilot extensions enabled."

# -------------------------------
# Reload VS Code
# -------------------------------
echo "Starting VS Code..."
code &

echo "Done! VS Code reset complete."
echo "Next steps:"
echo "1. Open Command Palette (Ctrl+Shift+P) → GitHub Copilot: Sign in"
echo "2. Sign in using your Student Pack GitHub account (Umairism)"
echo "3. Verify Copilot status → GitHub Copilot: Show Status"