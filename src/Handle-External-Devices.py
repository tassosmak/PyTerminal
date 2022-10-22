import os
def check():
    ask_if_stay=input("Another Device is Running in The same network\ndo you want to keep working here\nif yes press y\n select")
    if ask_if_stay == "y" or ask_if_stay == "Y":
        os.system("killall python")

check()