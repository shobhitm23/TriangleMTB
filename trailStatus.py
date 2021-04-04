import requests
from bs4 import BeautifulSoup

def getWebPage():

    info = requests.get("https://www.trianglemtb.com/mobiletrailstatus.php")
    soup = BeautifulSoup(info.content, 'html.parser')

    results = soup.findAll('a')

    with open('OUTPUT.html','w') as outfile:
        for x in results:

            final_str =  x.contents[0].strip()
            print(final_str)
            outfile.write(final_str + "\n")

getWebPage()


