#option to choose multiple osu accounts + modes
#menu
#ANOTHER profile
import json
import urllib.request
import os
import pickle
import time
from bs4 import BeautifulSoup

def aduser():
        while 0==0:
            time.sleep(0.4)
            link =  input("""What Is The Profile Link?
>>> """)
            OsuData = link
            try:
                OpenOsuData = urllib.request.urlopen(OsuData)
                soup = BeautifulSoup(OpenOsuData, "html.parser")
                namejsonraw = (soup.find('script', id="json-user").text)
                namejsonload = json.loads(namejsonraw)
                nameclean = (namejsonload['username'])
                while 0==0:
                    namecorr = input("The Name Of This User Is " + nameclean + """. Is This The One You Were Looking For?
Yes Or No
>>> """)
                    namecorr = namecorr.lower()
                    if namecorr == "yes":
                        return(nameclean, OsuData)
                    elif namecorr == "no":
                        print("Okay, Let's Try Again")
                        time.sleep(0.4)
                        break
                    else:
                        print("Sorry, I Didn't Quite Get That. Please Try Again")
                        break
                        
            except ValueError:
                print("Sorry, Not A Valid Link. Just Copy Paste Your Profile Link!")
                time.sleep(0.5)


if not os.path.exists("C:/Matissave/SaveMaster.pickle"):
    if not os.path.exists("C:/Matissave/"):
        os.makedirs("C:/Matissave/")
    maindata = {
        "osu": {
            }
        }
    breakmain = False
    typetext = """Do You Want To Analyze A Profile?
"""           
    while 0==0:
        time.sleep(0.4)
        yesorno = input(typetext + """Yes Or No
>>> """)
        yesorno = yesorno.lower()
        if yesorno == "yes":
            nameu, prolink = aduser()
            typetext = """Do You Want To Analyze Another Profile?
"""
            maindata['osu'][nameu] = {'link': prolink}
        elif yesorno == "no":
            break
        else:
            print("Sorry, I Didn't Quite Get That. Please Try Again")
            
    with open("C:/Matissave/SaveMaster.pickle", "wb") as f:
        pickle.dump(maindata, f)


userpath = (os.environ['USERPROFILE'])
if not os.path.exists(userpath + "/AppData/Roaming/Microsoft\
/Windows/Start Menu/Programs/Startup/osuscrape.pyw"):
    with open(userpath + "/AppData/Roaming/Microsoft\
/Windows/Start Menu/Programs/Startup/osuscrape.pyw", 'w') as f:
        f.write("""import json
import urllib.request
import os
import pickle
import time
from bs4 import BeautifulSoup

def sec_to_hrs(websec):
    webhrs = websec * float(0.0002777777777777777777777)
    return webhrs

with open("C:/Matissave/SaveMaster.pickle", "rb") as f:
    maindata = pickle.load(f)
            
links = []
osuname = []
for i in maindata['osu']:
    for l in [i]:
        osuname.append(l)
        links.append(maindata['osu'][l]['link'])


with open("C:/osuscrape/scrapedata.pickle", "rb") as f:
        lastwrite = pickle.load(f)

timecheck = lastwrite['osu']['']

while 0==0:
    timenow = time.strftime("%Y/%m/%d")
    hrnow = time.strftime("%H")
    if hrnow == "18":
        for profile in links:
            OsuData = profile
            OpenOsuData = urllib.request.urlopen(OsuData)
            soup = BeautifulSoup(OpenOsuData, "html.parser")
            secs = (soup.find('script', id="json-statistics").text)
            secs = json.loads(secs)
            secs = (secs['play_time'])

            hours = sec_to_hrs(secs)
            hours = int(hours)

            with open("C:/osuscrape/scrapedata.pickle", "rb") as f:
                osutree = pickle.load(f)

            osutree['osu'][osuname[links.index(profile)]] = {'links': ['']}
            osutree['osu'][osuname[links.index(profile)]]
            osutree['osu'][osuname[links.index(profile)]]
            osutree['osu']['settings']
            
            with open("C:/osuscrape/scrapedata.pickle", "wb") as f:
                pickle.dump(osutree, f)
    time.sleep(3400)
""")

#main
while 0==0:
    command = input("""What Do You Want To Do? Supported Commands Are:
Adprofile
Exit
>>> """)
    command = command.lower()
    if command == "exit":
        break
    elif command == "adprofile":
        breakmain = False
        typetext = """Do You Want To Analyze A Profile?
"""
        with open("C:/Matissave/SaveMaster.pickle", "rb") as f:
            maindata = pickle.load(f)
        
        while 0==0:
            time.sleep(0.4)
            yesorno = input(typetext + """Yes Or No
>>> """)
            yesorno = yesorno.lower()
            if yesorno == "yes":
                nameu, prolink = aduser()
                typetext = """Do You Want To Analyze Another Profile?
"""
                maindata['osu'][nameu] = {'link': prolink}
            elif yesorno == "no":
                break
            else:
                print("Sorry, I Didn't Quite Get That. Please Try Again")
        
        with open("C:/Matissave/SaveMaster.pickle", "wb") as f:
            pickle.dump(maindata, f)

    else:
        print("Sorry, I Didn't Quite Get That. Please Try Again")

