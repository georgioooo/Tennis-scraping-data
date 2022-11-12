from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd
import time
import re


year = 2019


def information(link_list):
    ranking = []
    name1 = []
    name2 = []
    winner_players = []
    loser_players = []
    winner_ranks = []
    loser_rank = []
    winner_age = []
    loser_age = []
    winner_height = []
    loser_height = []
    winner_titles = []
    loser_titles = []
    winner_h2h = []
    loser_h2h = []
    winner_hand = []
    loser_hand = []
    winner_weight = []
    loser_weight = []
    winner_YTD_Won_Lost = []
    loser_YTD_Won_Lost = []
    winner_YTD_Titles = []
    loser_YTD_Titles = []
    winner_CAREER_W_L = []
    loser_CAREER_W_L = []
    winner_Career_Prize_Money = []
    loser_Career_Prize_Money = []

    for item in link_list:
        html1 = 'https://www.atptour.com/en/players/atp-head-2-head' + item
        req = Request(html1, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req)
        soup = BeautifulSoup(webpage, 'html.parser')

        # Collecting Ranks of the players
        rank = soup.findAll('div', attrs={'class': 'head-to-head-rank-text'})
        for element in rank:
            ranking.append(element.text)

        # Collecting hands of the players
        r = soup.find_all('td')
        if len(r[12].text.strip('\r\n, \r\n')) > 0:
            winner_h = r[12].text.strip('\r\n, \r\n')[0]
            winner_hand.append(winner_h)
        else:
            winner_hand.append("")
        if len(r[14].text.strip('\r\n, \r\n')) > 0:
            loser_h = r[14].text.strip('\r\n, \r\n')[0]
            loser_hand.append(loser_h)
        else:
            loser_hand.append("")

        if len(r[9].text.strip('\r\n, \r\n')) > 0:
            winner_weight.append(r[9].text.strip('\r\n, \r\n')[0:3])
        else:
            winner_weight.append(0)

        if len(r[11].text.strip('\r\n, \r\n')) > 0:
            loser_weight.append(r[11].text.strip('\r\n, \r\n')[0:3])
        else:
            loser_weight.append(0)

        winner_YTD_Won_Lost.append(r[21].text.strip('\r\n, \r\n'))
        loser_YTD_Won_Lost.append(r[23].text.strip('\r\n, \r\n'))

        winner_YTD_Titles.append(r[24].text.strip('\r\n, \r\n'))
        loser_YTD_Titles.append(r[26].text.strip('\r\n, \r\n'))

        winner_CAREER_W_L.append(r[27].text.strip('\r\n, \r\n'))
        loser_CAREER_W_L.append(r[29].text.strip('\r\n, \r\n'))

        winner_Career_Prize_Money.append(r[33].text.strip('\r\n, \r\n'))
        loser_Career_Prize_Money.append(r[35].text.strip('\r\n, \r\n'))

        # Collecting names of the players
        first_name = soup.findAll('span', attrs={'class': 'first-name'})
        last_name = soup.findAll('span', attrs={'class': 'last-name'})
        for element in first_name:
            name1.append(element.text.strip("\r\n, \r\n "))

        for element in last_name:
            name2.append(element.text.strip("\r\n, \r\n "))

        # collecting head to head matchs
        left_H2H = []
        right_H2H = []
        right_player = soup.find('div', attrs={'class': 'h2h-player-right'})
        left_player = soup.find('div', attrs={'class': 'h2h-player-left'})
        for element1, element2 in zip(left_player, right_player):
            left_H2H.append(element1.text.strip("\n\r\n "))
            right_H2H.append(element2.text.strip("\n\r\n "))
        winner_h2h.append(left_H2H[3][0])
        loser_h2h.append(right_H2H[3][0])

        # to collect all data in the table <age>, <height>, ....
        data = []
        table = soup.find('table', attrs={'class': 'h2h-table h2h-table-ytd'})
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')

        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])  # Get rid of empty values

        winner_age.append(data[0][0][0:2])
        loser_age.append(data[0][2][0:2])

        x = data[2][0]
        pattern1 = re.compile(r"\([a-zA-Z0-9\ ]+\)")
        if len(pattern1.findall(x)) > 0:
            winner_height.append(pattern1.findall(x)[0][1:4])
        else:
            winner_height.append("")

        y = data[2][2]
        pattern2 = re.compile(r"\([a-zA-Z0-9\ ]+\)")
        if len(pattern2.findall(y)) > 0:
            loser_height.append(pattern2.findall(y)[0][1:4])
        else:
            loser_height.append("")

        if len(data[10]) > 0:
            winner_titles.append(data[10][0])
        else:
            winner_titles.append(0)

        if len(data[10]) > 2:
            loser_titles.append(data[10][2])
        else:
            loser_titles.append(0)

        time.sleep(30)

    names = []
    for val1, val2 in zip(name1, name2):
        names.append(val1 + " " + val2)

    for i in range(len(names)):
        if i % 2 == 0:
            winner_players.append(names[i])
            winner_ranks.append(ranking[i])
        elif i % 2 != 0:
            loser_players.append(names[i])
            loser_rank.append(ranking[i])

    winner_players.reverse()
    loser_players.reverse()
    winner_ranks.reverse()
    loser_rank.reverse()
    winner_age.reverse()
    loser_age.reverse()
    winner_height.reverse()
    loser_height.reverse()
    winner_titles.reverse()
    loser_titles.reverse()
    winner_h2h.reverse()
    loser_h2h.reverse()
    winner_hand.reverse()
    loser_hand.reverse()
    winner_weight.reverse()
    loser_weight.reverse()
    winner_YTD_Won_Lost.reverse()
    loser_YTD_Won_Lost.reverse()
    winner_YTD_Titles.reverse()
    loser_YTD_Titles.reverse()
    winner_CAREER_W_L.reverse()
    loser_CAREER_W_L.reverse()
    winner_Career_Prize_Money.reverse()
    loser_Career_Prize_Money.reverse()

    return winner_players, loser_players, winner_ranks, loser_rank, winner_age, loser_age, winner_height, \
           loser_height, winner_titles, loser_titles, winner_h2h, loser_h2h, winner_hand, loser_hand, winner_weight, \
           loser_weight, winner_YTD_Won_Lost, loser_YTD_Won_Lost, winner_YTD_Titles, loser_YTD_Titles, \
           winner_CAREER_W_L, loser_CAREER_W_L, winner_Career_Prize_Money, loser_Career_Prize_Money


table = pd.DataFrame()


html = 'https://www.atptour.com/en/scores/results-archive?year=year'
req = Request(html, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req)
soup = BeautifulSoup(webpage , 'html.parser')

data = []
new_data = []
court = []
surface = []
name = soup.findAll('td', attrs={'class': 'tourney-details'})
for element in name:
        data.append(element.text.strip(" \r\n "))

for i in range(1,len(data), 5):
    new_data.append(data[i].replace("\r\n", "").replace("                                                           "
                                                        "                         ", " "))

for i in range(len(new_data)):
    court.append(new_data[i].split()[0])
    surface.append(new_data[i].split()[1])

dates_des_tournois = []
tournament_date = soup.findAll('span', attrs={'class': 'tourney-dates'})
for element in tournament_date:
    dates_des_tournois.append(element.text.strip("\r\n "))


new = []
tournament_name = []
name = soup.findAll('span', attrs={'class': 'tourney-location'})
for element in name:
    new.append(element.text.strip())
for element in new:
    tournament_name.append(element.split(",")[0])


liste_des_nombres = []
classes = soup.findAll('td', attrs={'class': 'title-content'})
for element in classes:
    for a in element.find_all('a', href=True):
        result = re.findall('[0-9]+', a['href'])
        liste_des_nombres.append(result[0])

for dates_des_tournois, tournament_name, court, surface, number in zip(dates_des_tournois, tournament_name, court,
                                                                       surface, liste_des_nombres[59:]):
    table1 = pd.DataFrame()

    html = 'https://www.atptour.com/en/scores/archive/delray-beach/' + number + '/' + str(year) + '/results'
    req = Request(html, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)
    soup = BeautifulSoup(webpage, 'html.parser')

    href = []
    html = soup.findAll('td', attrs={'class': 'day-table-button'})
    for element in html:
        for a in element.find_all('a', href=True):
            href.append(a['href'])

    list_of_link = []
    for item in href:
        if 'players' in item:
            new_item = item[27:]
            list_of_link.append(new_item)

    x = information(list_of_link)

    liste_dates = [dates_des_tournois for i in range(len(x[1]))]
    liste_tournament = [tournament_name for i in range(len(x[1]))]
    liste_court = [court for i in range(len(x[1]))]
    liste_surface = [surface for i in range(len(x[1]))]

    table1['Date'] = liste_dates
    table1['Tournament'] = liste_tournament
    table1['Court'] = liste_court
    table1['Surface'] = liste_surface
    table1['Wrank'] = x[2]
    table1['Lrank'] = x[3]
    table1['Wage'] = x[4]
    table1['Lage'] = x[5]
    table1['Wheight'] = x[6]
    table1['Lheight'] = x[7]
    table1['Wtitles'] = x[8]
    table1['Ltitles'] = x[9]
    table1['Wh2h'] = x[10]
    table1['Lh2h'] = x[11]
    table1['winner_hand'] = x[12]
    table1['loser_hand'] = x[13]
    table1['winner_weight'] = x[14]
    table1['loser_weight'] = x[15]
    table1['winner_YTD_Won_Lost'] = x[16]
    table1['loser_YTD_Won_Lost'] = x[17]
    table1['winner_YTD_Titles'] = x[18]
    table1['loser_YTD_Titles'] = x[19]
    table1['winner_CAREER_W_L'] = x[20]
    table1['loser_CAREER_W_L'] = x[21]
    table1['winner_Career_Prize_Money'] = x[22]
    table1['loser_Career_Prize_Money'] = x[23]
    table1['Winner'] = x[0]
    table1['Loser'] = x[1]

    table = table.append(table1, ignore_index=True)
    table.to_csv('out.csv', index=False)