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

coloringPrint = colored.fore.LIGHT_SKY_BLUE_3B + colored.style.BOLD
coloringSecret = colored.fore.LIGHT_YELLOW

__________ = "Extbhite"
___________________ = "1.2.58"
_________________ = f"""
{__________}. (Telegram: https://t.me/Extbhite or @Extbhite)
{___________________}
If you downloaded the script from other resource not in GitHub page - delete this. You can get hacked.
"""

print(coloringSecret + _________________)

def NotFoundedVideoChatError():
    """Script error if you didn't start video chat."""
    print("\nCan't find video chat or you not starting.\n")

def ClaimedReputationText(repupationGetInfo: str, YourTotalReputationInfo: str):
    """Claim reputation text, if this printed - you get reputation."""
    print(f"""
Claimed video rep.

[INFO]
Getting reputation >> {repupationGetInfo}
Your total reputation >> {YourTotalReputationInfo}
        """)

def scriptMenuUtilites(version: str, nameScript: str, authorScript: str):
    """For design the script."""
    print(coloringPrint + pyfiglet.figlet_format(f"{nameScript}"))
    print(f"""
Script by {authorScript}
Version of script: {version}
    """)