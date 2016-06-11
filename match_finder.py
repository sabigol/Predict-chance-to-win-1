from bs4 import BeautifulSoup
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
        odda = soup.select(".odds .odd")
        print(odda)