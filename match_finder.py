from __future__ import print_function
from bs4 import BeautifulSoup
import pymysql
import requests


class MatchFinder:

    def __init__(self, page_url):
        super().__init__()
        self.page_url = page_url

    def fetch_matchs(self):
        request = requests.get(self.page_url)
        data = request.text
        soup = BeautifulSoup(data, "html.parser")
        self.get_tablesleague(soup)

    def error(self, message):
        pass

    def get_tablesleague(self, soup):
        teama = soup.select(".row .name > a > .teama")
        print(teama)
        teamb = soup.select(".row .name > a > .teamb")
        print(teamb)
        date = soup.select(".row .date > .date_i")
        print(date)
        odda = soup.select(".odds > div:nth-of-type(1)")
        oddx = soup.select(".odds > div:nth-of-type(2)")
        oddb = soup.select(".odds > div:nth-of-type(3)")
        print(odda)
        print(oddx)
        print(oddb)
        for i in range(len(date)):
            if odda[i].text != '-':
                if oddx[i].text != '-':
                    if oddb[i].text != '-':
                        self.insert_item(date[i].text, teama[i].text, teamb[i].text, odda[i].text, oddx[i].text, oddb[i].text)

    def insert_item(self, date, teama, teamb, preda, predx, predb):
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               passwd='root',
                               db='predictor',
                               autocommit=True)
        cur = conn.cursor()
        cur.execute("INSERT INTO `matches` VALUES ('" + str(date) + "', '" +
                    str(teama) + "', '" +
                    str(teamb) + "', '" +
                    str(preda) + "', '" +
                    str(predx) + "', '" +
                    str(predb) + "')")
        cur.close()
        conn.close()
        # self.see_db();

    @staticmethod
    def see_db():
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               passwd='root',
                               db='predictor',
                               autocommit=True)
        cur = conn.cursor()
        cur.execute("SELECT * FROM `matches`")
        print(cur.description)
        for row in cur:
            print(row)
        cur.close()
        conn.close()

