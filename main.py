import time
import pyfiglet
from termcolor import colored
from colorama import init

# Initialize colorama for Windows compatibility
init()

def typewriter_effect(text, delay=0.05):
    """Prints text with a typewriter effect."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def cool_hello():
    """Prints a cool 'Hello!' with ASCII art and colors."""
    # Generate ASCII text
    ascii_text = pyfiglet.figlet_format("Hello!")

    # Print ASCII text in green
    print(colored(ascii_text, "green"))

    # Print a stylish typewriter message
    typewriter_effect(colored("Welcome to the world of Jenkins! 🚀", "cyan"))

if __name__ == "__main__":
    cool_hello()
