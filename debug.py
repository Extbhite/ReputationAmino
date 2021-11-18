from terminal_configs import debugmenu
import os
try:
    import pyfiglet
except ModuleNotFoundError:
    os.system("pip install pyfiglet")
    import pyfiglet
try:
    import colored
except ModuleNotFoundError:
    os.system("pip install colored")
    import colored

class TerminalStructure(): # // Хоть class был использован неправильно или правильно, но мне чертовки не удобно пихать каждые def в один def..

    def pathTextTerminal(textLogoTerminal: str = None):

        if textLogoTerminal:
            print(colored.fore.SKY_BLUE_3 + pyfiglet.figlet_format(f"{textLogoTerminal}"))

    def commandsInput():
        while True:
            choose = input("$repamino/debug >> ") # // By this input, you can type commands.

            if choose == "helpdebug":
                commandList = [
                    'helpdebug', # // Show commands.
                    'installrequirements -r requirements.txt', # // Installing requirements for script.
                    'credits', # // Copyright okay?
                    'script --list', # // Showing script list.
                    'script --start <main.py, join_vc.py>' # // Starting scripts with one choice.
                ]
                print(f"Commands: {commandList}")
            
            elif choose == "installrequirements -r requirements.txt":
                os.system("pip install -r requirements.txt")
                os.system("clear")
                main()

            elif choose == "credits":
                os.system("start credits.txt")
            
            elif choose == "script --start main.py":
                os.system("clear")
                os.system("python main.py")
                
            elif choose == "script --start join_vc.py":
                os.system("clear")
                os.system("python join_vc.py")
                
            elif choose == "script --list":
                list = [
                    'main.py',
                    'debug.py',
                    'join_vc.py',
                    'apprep.py(For PC users)'
                ]
                print(list)

def main():
    TerminalStructure.pathTextTerminal(textLogoTerminal="Debug")
    debugmenu.startTerminalText()
    TerminalStructure.commandsInput()

if __name__ == "__main__":
    main()
