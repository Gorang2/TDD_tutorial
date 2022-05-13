import requests
from bs4 import BeautifulSoup

class Crawler :
    def __init__(self, url, keyword):
        self.result = []
        self.url = url
        self.keyword= keyword
        self.html_lst = []

    def crawl(self):
        response = requests.get(self.url)

        if response.status_code != 200: 
         print(response.status_code)
        else :
            html = response.text
            soup = BeautifulSoup(html, "html.parser")
            self.html_lst = str(soup.body).replace(">", "<").split("<")
            self.find_keyword()

    def find_keyword(self):
            for i in self.html_lst:
                if self.keyword in i:
                    self.result.append(i)

    def getResult(self):
        if len(self.result) == 0:
            return False
        return self.result