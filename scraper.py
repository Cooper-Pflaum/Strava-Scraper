import pandas as pd
import asyncio
import re
from bs4 import BeautifulSoup
from Colors import *
from pyppeteer import launch



async def get_html(club_id):
    url = f'https://www.strava.com/clubs/{club_id}/leaderboard'

    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    await page.waitForSelector("td.distance", visible=True)
    html = await page.content()
    await browser.close()
    return html

def get_club_distance(soup):
    distances = []
    for dist in soup.select('td.distance'):
        dist_as_a_num = float(re.findall("\d+\.\d+", str(dist))[0])
        distances.append(dist_as_a_num)
        
        
    i = 0
    total_dist = 0
    for dist in distances:
        
        # dist_number = 
        print(f'{i+1}: {round(dist, 1)}km or {round((dist)/1.609, 1)}mi')
        # print(i)
        i+=1
        total_dist += dist
    
    print(colors.green + 'Total Weekly Distance: ' + str(round(total_dist,1)) +'km/' + str(round((total_dist)/1.609, 1)) + 'mi' + colors.reset)
    return distances, total_dist
    
def get_club_ranks(soup):
    athletes = []
    for athlete in soup.select('a.athlete-name'):
        # athlete_name = str(soup.select('a.athlete-name'))
        name = str(athlete)[59:str(athlete).index('.')+1]
        
        if '\n' in name:
           name = name[1:]
        athletes.append(name)
    del athletes[:9]
    print(colors.green + str(athletes) + colors.reset)

# # get_club_distances()
# get_club_ranks()

