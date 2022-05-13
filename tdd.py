import requests
from bs4 import BeautifulSoup

class Crawler :
    def __init__(self, url, phrase_to_find):
        self.result = []
        self.url = url
        self.phrase_to_find= phrase_to_find
        self.html_lst = []

    def crawl(self):
        response = requests.get(self.url)

        if response.status_code != 200: 
         print(response.status_code)
        else :
            html = response.text
            soup = BeautifulSoup(html, "html.parser")
            self.html_lst = str(soup.body).replace(">", "<").split("<")
            self.find_phrase()

    def find_phrase(self):
            for i in self.html_lst:
                if self.phrase_to_find == i:
                    self.result.append(i)

    def getResult(self):
        if len(self.result) == 0:
            return False
        return self.result