from tdd import Crawler
import unittest
class CrawlerTester(unittest.TestCase) :
    def test_phrase(self):
        print("========== Test1 : finding phrase in html ============")
        crwler = Crawler("http://naver.com", "네이버를 시작페이지로")
        crwler.crawl()
        self.assertEqual(["네이버를 시작페이지로"], crwler.getResult())

if __name__ == '__main__':
    unittest.main()