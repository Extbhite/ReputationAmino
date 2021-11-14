# // deviceId: 177910677f61e347778c8c13df7b069feb134bb11747c1ad4507c361af09a060b83fc15d22cb3f4468 (For you)
import os
def installRequirements():
    print("[STATUS: START DEBUG]")
    os.system("python debug.py")

try:
    import amino
except ModuleNotFoundError:
    installRequirements()
    import amino
from threading import Thread
from time import sleep
from utilites import NotFoundedVideoChatError, ClaimedReputationText, scriptMenuUtilites

chatlist = []
chatnames = {}

def functionScriptRep(emailLogin: str, passwordLogin: str):
    scriptMenuUtilites(version="1.2.1", nameScript="ReputationFarm", authorScript="Extbhite")
    client = amino.Client() # // Client.
    email = f"{emailLogin}" # // Paste email in here.
    password = f"{passwordLogin}" # // Paste password in here.
    client.login(email=email, password=password) # // Login in to your account.
    print("Successfully log in.")

    # // TODO: Making the claim rep video function in amino_new lib.
    com_list = client.sub_clients(size=100)
    for i, name in enumerate(com_list.name, 1):
        print(f"{i} > {name}")
    ndcId = com_list.comId[int(input("Выбери сообщество/Choose the community >> "))-1]

    local = amino.SubClient(comId=ndcId, profile=client.profile) # // Local.
    z=0
    chat_list = local.get_chat_threads(start=0 ,size=1000)
    print("")
    for title, id in zip (chat_list.title, chat_list.chatId):
        print(f"{z + 1}.{title}")  
        chatnames[i]=str(title)
        chatlist.append(str(id))
        z+=1
    objectId = chatlist[int(input("Выбери чат/Choose the chat >> "))-1]
    def videoRep():
        rep = local.get_vc_reputation_info(chatId=objectId).availableReputation # // Getting video rep info.
        yourRep = local.get_vc_reputation_info(chatId=objectId).reputation # // Getting video rep info.
        try:
            local.claim_vc_reputation(chatId=objectId) # // claim_vc_reputation function.
            ClaimedReputationText(repupationGetInfo=rep, YourTotalReputationInfo=yourRep) # // Informating by getting reputation.
        except Exception as e:
            NotFoundedVideoChatError()
            print(e)

    while True:
        Thread(target=videoRep).start() # // Threading this function to fasted.
        sleep(0.08) # // Cooldown.