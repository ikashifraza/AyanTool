
#!/bin/bash
# AYAN TOOL INSTALLER SCRIPT

echo -e "\033[1;92m[*] Removing any previous version of AyanTool...\033[0m"
rm -rf AyanTool

echo -e "\033[1;96m[*] Cloning latest version from GitHub...\033[0m"
git clone https://github.com/ikashif_raza/AyanTool

cd AyanTool

echo -e "\033[1;92m[*] Launching AYAN TOOL...\033[0m"
python AYAN_TOOL_COOL.py
