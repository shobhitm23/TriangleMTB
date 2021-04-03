import requests

def getWebPage():

    info = requests.get("https://www.trianglemtb.com/mobiletrailstatus.php")
    print(info.content)

    with open('OUTPUT.txt','w') as outfile:
        outfile.write(info.text)

getWebPage()