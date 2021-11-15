#Copyright [2021-2031] [Extbhite]
from terminal_configs import menu, repConfig
import os

menu.startTerminalText()

def joinVcMain():
    os.system("python join_vc.py")
    main()

def credits():
    print("""
Script by Extbhite
Telegram - @Extbhite

Coryright you can see full in credits.txt file. (c)
    """)
    os.system("clear")
    main()

def main():
    choose = input(">> ")

    if choose == "1":
        menu.scriptsMenuList()
        scriptschoose = input(">> ")

        if scriptschoose == "1":
            email = input("Email >> ")
            password = input("Password >> ")
            repConfig.functionScriptRep(emailLogin=email, passwordLogin=password)

        elif scriptschoose == "2":
            joinVcMain()
            
        elif scriptschoose == "0":
            menu.chooseMenuText()
            main()

    elif choose == "2":
        credits()

    elif choose == "3":
        print("Exited from script.\n\nPress Enter to close.")
        input("")

    # // TODO: Making debug choosing and script.
    elif choose == "d":
        os.system("clear")
        os.system("python debug.py")

if __name__ == "__main__":
    main()
