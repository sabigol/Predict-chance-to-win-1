#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from mysql_connector import MySQLConnector
import bs4
import requests


class MatchFinder:

    def __init__(self, page_url):
        self.page_url = page_url

    def fetch_matchs(self):
        request = requests.get(self.page_url)
        data = request.text
        soup = bs4.BeautifulSoup(data, "html.parser")
        get_tablesleague(soup)

    def error(self, message):
        pass


def get_tablesleague(soup):
    teama = soup.select(".row .name > a > .teama")
    # print(teama)
    teamb = soup.select(".row .name > a > .teamb")
    # print(teamb)
    date = soup.select(".row .date > .date_i")
    # print(date)
    odda = soup.select(".odds > div:nth-of-type(1)")
    oddx = soup.select(".odds > div:nth-of-type(2)")
    oddb = soup.select(".odds > div:nth-of-type(3)")
    # print(odda)
    # print(oddx)
    # print(oddb)
    for i in range(len(date)):
        if odda[i].text != '-':
            if oddx[i].text != '-':
                if oddb[i].text != '-':
                    print("Data i godzina: " + date[i].text + ", (" +
                          odda[i].text + ") " +
                          teama[i].text + " - " +
                          teamb[i].text + ", (" +
                          oddb[i].text + "), Szansa na remis: " +
                          oddx[i].text)
        # conn = MySQLConnector()
        # conn.insert_item(date[i].text, teama[i].text, teamb[i].text, odda[i].text, oddx[i].text, oddb[i].text)
