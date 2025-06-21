
import os
import time

# Colors
RED = "\033[1;91m"
GREEN = "\033[1;92m"
YELLOW = "\033[1;93m"
BLUE = "\033[1;94m"
CYAN = "\033[1;96m"
RESET = "\033[0m"

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def loading():
    msg = f"{CYAN}Initializing AYAN Tool"
    for i in range(3):
        print(msg + "." * (i + 1))
        time.sleep(0.5)
        clear()

def banner():
    print(f"""
{GREEN}
 █████╗ ██╗   ██╗ █████╗ ███╗   ██╗
██╔══██╗██║   ██║██╔══██╗████╗  ██║
███████║██║   ██║███████║██╔██╗ ██║
██╔══██║██║   ██║██╔══██║██║╚██╗██║
██║  ██║╚██████╔╝██║  ██║██║ ╚████║
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝
      {YELLOW}💥 TOOL BY AYAN 💥{RESET}
    """)

def menu():
    clear()
    banner()
    print(f"{BLUE}Welcome to {YELLOW}AYAN MultiTool{RESET}!")
    print(f"{CYAN}Use this tool responsibly ✌️{RESET}\n")
    print(f"{GREEN}[1] Start Cloning")
    print(f"{GREEN}[2] About Tool")
    print(f"{RED}[0] Exit{RESET}")

def about():
    clear()
    banner()
    print(f"{YELLOW}This tool is created by AYAN for educational purposes only.{RESET}")
    input(f"\n{BLUE}Press Enter to return to menu...{RESET}")
    main()

def main():
    while True:
        menu()
        choice = input(f"\n{YELLOW}Select an option: {RESET}")
        if choice == '1':
            print(f"\n{RED}[!] Cloning module is under construction...{RESET}")
            time.sleep(2)
        elif choice == '2':
            about()
        elif choice == '0':
            print(f"{GREEN}Goodbye!{RESET}")
            break
        else:
            print(f"{RED}Invalid choice! Please try again.{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    loading()
    main()
