import requests
from bs4 import BeautifulSoup
import json

def getWebPage():

    list_of_trails = []
    list_stats = []
    trail_stats = {}

    info = requests.get("https://www.trianglemtb.com/mobiletrailstatus.php")
    soup = BeautifulSoup(info.content, 'html.parser')

    results_trails = soup.findAll('a')
    results_stats_open = soup.findAll('td', class_='info')
    results_stats_closed = soup.findAll('td', class_='closed')

    for x in results_trails[:-1]:
        final_str =  x.contents[0].strip()
        final_str = ''.join(e for e in final_str if e.isalnum())
        list_of_trails.append(final_str)
    
    for t in soup.findAll('tr'):
        sentence = str(t.text)

        if 'OPEN' in sentence:
            list_stats.append("OPEN")

        elif 'CLOSED' in sentence:
            list_stats.append("CLOSED")

    index = 0
    for trail in list_of_trails:
        trail_stats[trail] = list_stats[index]
        index += 1

    print(trail_stats)

    with open('OUTPUT.json', 'w') as outfile:
        json.dump(trail_stats, outfile, indent=4)

getWebPage()


