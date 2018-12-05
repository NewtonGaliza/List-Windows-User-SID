import os

def getUserInfo():	
    users = os.system('wmic useraccount get name')
    sid = os.system('wmic useraccount get sid')
    return users
    return sid
    
getUserInfo()
