# !!
# // STEALED THIS SCRIPT FROM PART TIMER SERVER //
# // DISCORD SERVER: https://discord.gg/PdZuuuNVpm //
# !!

from amino import Client # Importing the client
from amino import SubClient # Importing the Subclient
from amino.lib.util.exceptions import * # Importing the exceptions
from concurrent.futures import ProcessPoolExecutor # Importing the Multiprocessing library
from concurrent.futures import ThreadPoolExecutor # Importing the Threading Library
from os import path # Importing the path to locate the current directory
import json # Importing json to read accounts data from accounts.json
THIS_FOLDER = path.dirname(path.abspath(__file__)) # Current Directory path
emailfile=path.join(THIS_FOLDER,"emails.json") # accounts.json file path
dictlist=[] # Empty list initialisation which will hold dictionaries from accounts.json
link=input("chat link: ")#blogId="ab1f62b3-45c2-4dce-8bbd-218d41804bab"
gg=Client().get_from_code(link)
cid=gg.path[1:gg.path.index("/")]
chatId=gg.objectId
with open(emailfile) as f: # Opening the accounts.json file
    dictlist = json.load(f) # Loading the dictionary list from accounts.json inside dictlist variable
#dicklis=dictlist.reverse()
def log(cli : Client,email : str, password : str): # Defining the log function which will log into the accounts
    try: # Tries to execute the intended code
        cli.login(email=email,password=password)
        print(f"logged in with {email}")# Logs in the client with email and password provided as arguments
     # Prints the email with incorret password
    except Exception as g:
        print(g)
def threadit(acc : dict): # Defining the main threading function which will run in a threaded loop
    #global totalcoin # Using the global variable totalcoin inside the block
    email=acc["email"] # Assigns the value of "email" key inside email variable
    device=acc["device"] # Assigns the value of "device" key inside device variable
    password=acc["password"] # Assigns the value of "password" key inside password variable
    client=Client(device) # Makes a client object of CLient class with device argument
    log(cli=client,email=email,password=password)
    client.join_community(comId=cid)
    sub=SubClient(comId=cid,profile=client.profile)
    sub.join_chat(chatId)
    client.join_video_chat_as_viewer(chatId=chatId,comId=cid)
    
    # Calls the log function defined with client,email and password as arguments
    #client.join_community(cid)
    print("verified")# Joins the community which was assigned
    

def main(): # defining the main function
    print(f"{len(dictlist)} accounts loaded") # Printing the total number of accounts inside accounts.json
    with ThreadPoolExecutor(max_workers=4) as executor:  # Makes a processpool executor with 60 workers at a time
        _ = [executor.submit(threadit, amp) for amp in dictlist] # Runs threadit for accounts from dictlist
    #print(f"Totan no. of coins is :- {totalCoin}") # Prints total no. of coins transferred

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
# Runs the main function
    
