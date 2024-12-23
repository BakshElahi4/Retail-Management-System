import pyfiglet
from colorama import Fore, Style, init

# Initialize colorama for cross-platform support
init(autoreset=True)

def print_welcome_message():
    # Generate ASCII art with a clearer font
    ascii_art = pyfiglet.figlet_format("eCommerce Shop", font="standard")
    
    # Print the stylized welcome message
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)
    print(Fore.MAGENTA + Style.BRIGHT + ascii_art)
    print(Fore.YELLOW + Style.BRIGHT + "       We offer various products and delivery options.      ")
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)


def print_loading_message():
    print(Fore.YELLOW + Style.BRIGHT + "Loading...")
