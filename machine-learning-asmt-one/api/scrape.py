# importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import requests

# headers are often used to gain access to an otherwise locked API
HEADERS = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-token': 'true',
    'Referer': 'http://stats.nba.com/player/',
    'Connection': 'keep-alive',
    'x-nba-stats-origin': 'stats'
}

# define function to be used
def get_data(url):
    response = requests.get(url, headers=HEADERS)
    while response.status_code != 200:
        response = requests.get(url)
    # explore the response in developers tools to find the proper arrangement of your json response
    headers = response.json()['resultSets'][0]['headers']
    data = response.json()['resultSets'][0]['rowSet']
    data = pd.DataFrame(data, columns=headers)
    return data

# define the url
url = 'http://stats.nba.com/stats/playerdashboardbyyearoveryear?DateFrom=&DateTo=&GameSegment=' \
      '&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=' \
      '&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID=201935&PlusMinus=N&Rank=N' \
      '&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&Split=yoy' \
      '&VsConference=&VsDivision='


# get the pandas data frame
data = get_data(url)

# once you have the data, you can save it simply to a csv
# to remove the index from the frame, indicate so as an argument
data.to_csv('player.csv', index=False)
