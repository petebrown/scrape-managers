from bs4 import BeautifulSoup
import datetime as dt
import pandas as pd
import requests

team_id = 2598

url = f'https://www.soccerbase.com/teams/team.sd?team_id={team_id}&teamTabs=managers'
r = requests.get(url)
doc = BeautifulSoup(r.text, 'html.parser')

managers = doc.select('#managers tbody tr')

manager_list = []
for manager in managers:
    manager_data = manager.select('td')
    
    manager_sb_id = manager_data[0].select_one('a')['href'].split('=')[1]
    
    manager_name = manager_data[0].text.strip()
    
    manager_start_date = manager_data[1].text
    manager_start_date = dt.datetime.strptime(manager_start_date, '%d %b, %Y')
    
    manager_end_date = manager_data[2].text
    if manager_end_date == 'Present':
        manager_end_date = dt.datetime.now().strftime('%Y-%m-%d')
    else:
        manager_end_date = dt.datetime.strptime(manager_end_date, '%d %b, %Y')
    
    manager_record = {
        'manager_sb_code': manager_sb_id,
        'manager_name': manager_name,
        'manager_start_date': manager_start_date,
        'manager_end_date': manager_end_date
    }

    manager_list.append(manager_record)

manual_updates = {
        'manager_sb_code': '1058',
        'manager_name': 'Ray Mathias',
        'manager_start_date': dt.datetime.strptime('1985-02-12', '%Y-%m-%d'),
        'manager_end_date': dt.datetime.strptime('1985-05-11', '%Y-%m-%d')
    }
    
manager_list.append(manager_record)

df = pd.DataFrame(manager_list).drop_duplicates().reset_index(drop = True)
df.to_csv('./data/managers_df.csv', index = False)