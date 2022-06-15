import mock
from tdd import Crawler
import unittest
from unittest.mock import Mock
class CrawlerTester(unittest.TestCase) :
    def test_phrase(self):
        print("========== Test1 : finding phrase in html ============")
        crwler = Crawler("http://naver.com", "네이버를 시작페이지로")
        crwler.crawl()
        self.assertEqual(["네이버를 시작페이지로"], crwler.getResult())
    
    def test_word(self):
        print("=========== Test2 : finding phrase that contains keyword in html===============")
        crwler = Crawler("http://naver.com", "정책")
        crwler.crawl()
        self.assertEqual(["네이버 정책 및 약관", '청소년보호정책', '네이버 정책'], crwler.getResult())

    def test_count(self):
        print("=============== Test3 : count the results ==============")
        crwler = Crawler("http://naver.com", "행복")
        mock = Mock(return_value= ["<p>행복하세요!</p>", "<p>행복하세요!</p>", "<p>행복하세요!</p>"])
        crwler.html_lst = mock()
        crwler.find_keyword()  
        self.assertEqual(3, crwler.getCount())
if __name__ == '__main__':
    unittest.main()
