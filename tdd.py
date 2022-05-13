import requests
from bs4 import BeautifulSoup
import unittest

class CrawlerTester(unittest.TestCase) :
    def test_phrase(self):
        print("========== Test1 : finding phrase in html ============")
        crwler = Crawler("http://naver.com", "네이버를 시작페이지로")
        crwler.crawl()
        self.assertEqual(["네이버를 시작페이지로"], crwler.getResult())


class Crawler :
    def __init__(self, url, keyword):
        self.result = []
        self.url = url
        self.keyword = keyword
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
                if self.keyword == i:
                    self.result.append(i)

    def getResult(self):
        if len(self.result) == 0:
            return False
        return self.result

if __name__ == '__main__':
    unittest.main()
