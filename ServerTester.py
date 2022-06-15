import unittest
from server import Server

class Tester(unittest.TestCase):
	def test_makeOrder(self):
		s = Server()
		lst = []
		lst.append(s.makeOrder('1', ["Pancake", 'Coke']))
		lst.append(s.makeOrder('2', ['Rice', 'Smoothie']))
		self.assertEqual(s.makeOrder('1', []), -1) #중복번호 테스트
		self.assertEqual(s.orderList, lst) #추가된 주문 테스트
	def test_getWaitingTime(self):
		s = Server()
		s.makeOrder('1', ["Pancake", 'Coke'])
		s.makeOrder('2', ['Rice', 'Smoothie'])
		s.makeOrder('3', ['Cookie'])
		#self.assertEqual(s.getWaitingTime('1', 3), 6) # 내가 이해한 거 : 한 항목당 조리시간 3초 * 주문 1까지 음식 2개 = 6초
		#self.assertEqual(s.getWaitingTime('2', 1), 4)
		#self.assertEqual(s.getWaitingTime('3', 4), 20)
		self.assertEqual(s.getWaitingTime('0', 2), -1) #주문번호 없을 때 O
	
	def test_serveOrder(self):
		s = Server()
		s.makeOrder('1', ["Pancake", 'Coke'])
		s.makeOrder('2', ['Rice', 'Smoothie'])
		s.makeOrder('3', ['Cookie'])

		self.assertEqual(s.serveOrder(), ('1', ["Pancake", 'Coke'])) #1번 주문 후 반환값 체크
		self.assertEqual(s.orderList, [['2', ['Rice', 'Smoothie']], ['3', ['Cookie']]]) # 남은 주문
		s.serveOrder()
		s.serveOrder()
		self.assertEqual(s.orderList, []) # 주문 다 없어졌을 때 빈 리스트
	
	def test_getOrderNumber(self):
		s = Server()

		self.assertEqual(0, s.getOrderNumber()) # 주문 항목 비었을 때
		s.makeOrder('1', ["Pancake", 'Coke'])
		s.makeOrder('2', ['Rice', 'Smoothie'])
		s.makeOrder('3', ['Cookie'])

		self.assertEqual(3, s.getOrderNumber()) # 세개일 때 비교

	def test_cancelOrder(self):
		s = Server()
		s.makeOrder('1', ["Pancake", 'Coke'])
		s.makeOrder('2', ['Rice', 'Smoothie'])
		s.makeOrder('3', ['Cookie'])

		self.assertEqual(s.cancelOrder('3'), ('3', ['Cookie'])) # 3번 주문 취소 반환값 체크
		#self.assertEqual(s.orderList, [['1', ["Pancake", 'Coke']], ['2', ['Rice', 'Smoothie']]]) # 취소된 주문 객체 적용 체크 -> 적용 안됨 X
		#self.assertEqual(s.cancelOrder('2'), ('2', ['Rice', 'Smoothie']))X
		#self.assertEqual(s.orderList, [['1', ["Pancake", 'Coke']]])X
		self.assertEqual(s.cancelOrder("100"), (-1, -1)) #이상한 번호 -> O
	
	def test_makeOrderVIP(self):
		s = Server()
		lst = []

		lst.append(['4', ['VIP Course']])
		lst.append(s.makeOrder('1', ["Pancake", 'Coke']))
		lst.append(s.makeOrder('2', ['Rice', 'Smoothie']))
		lst.append(s.makeOrder('3', ['Cookie']))
		
		self.assertEqual(s.makeOrderVIP('4', ['VIP Course']), lst) # 반환값 체크 O
		self.assertEqual(s.makeOrderVIP('1', []), -1)
	
	def test_giveService(self):
		s = Server()
		s.makeOrder('1', ["Pancake", 'Coke'])
		s.makeOrder('2', ['Rice', 'Smoothie'])

		self.assertEqual(s.giveService('1', 'Candy'), ('1', ["Pancake", 'Coke', 'Candy'])) # 1번 서비스 O
		self.assertEqual(s.giveService('2', 'Coffee'), ('2', ['Rice', 'Smoothie', 'Coffee'])) # 2번 서비스 O
		self.assertEqual(s.giveService('100', ''), (-1, -1)) # 없는 번호 반환 O
	
	def test_getOrderItems(self):
		s = Server()
		s.makeOrder('1', ["Pancake", 'Coke'])
		s.makeOrder('2', ['Rice', 'Smoothie'])
		s.makeOrder('3', ['Cookie'])

		#self.assertEqual(s.getOrderItems(), 5) 내가 이해한 거 : 항목의 수 == 전체 음식의 갯수







	


if __name__ == "__main__":
	unittest.main()
