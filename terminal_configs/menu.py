import os
def installRequirements():
    print("[STATUS: START DEBUG]")
    os.system("python debug.py")

try:
    import pyfiglet
except ModuleNotFoundError:
    installRequirements()
    import pyfiglet
try:
    import colored
except ModuleNotFoundError:
    installRequirements()
    import colored

# // Colors
skyBlue = colored.fore.CYAN_3
# // Colors

def startTerminalText():
    print(skyBlue + pyfiglet.figlet_format("Rep\nFarm"))
    print("""Thanks for using this script!
You can choose next numbers:

[1] Scripts start.
[2] Credits.
[3] Exit from script.
[d] Start debug mode.(terminal)
""")

def alreadyUsedTerminalText():
    print(skyBlue + pyfiglet.figlet_format("Rep\nFarm"))
    print("""[1] Scripts start.
[2] Credits.
[3] Exit from script.
[d] Start debug mode.(terminal)
""")

def scriptsMenuList():
    print("""
[1] Start "repConfig.py" script.
[2] Start "join_vc.py" script.
[0] Back to menu.
    """)
    
def chooseMenuText():
    print("""
[1] Scripts start.
[2] Credits.
[3] Exit from script.
[d] Start debug mode.(terminal)
    """)