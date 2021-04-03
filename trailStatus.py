import requests

def getWebPage():

    info = requests.get("https://www.trianglemtb.com/mobiletrailstatus.php")

    with open('OUTPUT.html','w') as outfile:
        outfile.write(info.text)

getWebPage()


