import csv
import unittest
from problem_remote import RemoteControl
#from 자기 파일명 import RemoteControl

class Tester(unittest.TestCase):
	def test_powerOnRemoteControl(self):
		rm = RemoteControl()
		self.assertEqual(rm.powerOnRemoteControl([[1, "SBS"]]), 1)
		self.assertEqual(rm.powerOnRemoteControl([[1, "SBS"], [2, "KBS"], [3, "JTBC"]]), 3)
		self.assertEqual(rm.powerOnRemoteControl([[1, "SBS"], [2, "KBS"], [3, "JTBC"], [4, "TVN"]]), 3)
	
	def test_goToChannel(self):
		rm = RemoteControl()
		rm.powerOnRemoteControl([[1, "SBS"], [2, "KBS"], [3, "JTBC"], [4, "TVN"]])
		self.assertEqual(rm.goToChannel(4), "TVN")
		self.assertEqual(rm.goToChannel(1), "SBS")
		self.assertEqual(rm.goToChannel(2), "KBS")
		self.assertEqual(rm.goToChannel(3), "JTBC")

	def test_nextChannel(self):
		rm = RemoteControl()
		rm.powerOnRemoteControl([[1, "SBS"], [2, "KBS"]])
		self.assertEqual(rm.nextChannel(), "KBS")
		self.assertEqual(rm.nextChannel(), "SBS")

	def test_previousChannel(self):
		rm = RemoteControl()
		rm.powerOnRemoteControl([[1, "SBS"], [2, "KBS"]])
		self.assertEqual(rm.previousChannel(), "KBS")
		self.assertEqual(rm.previousChannel(), "SBS")
	
	def test_blockUnblock(self):
		rm = RemoteControl()
		rm.powerOnRemoteControl([[1, "SBS"], [2, "KBS"]])
		self.assertEqual(rm.blockChannel(), "KBS")
		self.assertEqual(rm.nextChannel(), "KBS")
		self.assertEqual(rm.unblockChannel(1), 1)
		self.assertEqual(rm.unblockChannel(100), -1) #실패 시 -1 반환
	
	def test_favorChannel_aiNextChannel(self):
		rm = RemoteControl()
		rm.powerOnRemoteControl([[1, "SBS"], [2, "KBS"], [3, "JTBC"]])
		rm.goToChannel(3)
		self.assertEqual(rm.favorChannel(), 1)
		rm.previousChannel()
		rm.favorChannel()
		rm.favorChannel()
		rm.previousChannel()
		self.assertEqual(rm.aiNextChannel(), 2)
		self.assertEqual(rm.aiNextChannel(), 3)

	def test_powerOffRemoteControl(self):
		rm = RemoteControl()
		rm.powerOnRemoteControl([[1, "SBS"], [2, "KBS"], [3, "JTBC"]])
		rm.powerOffRemoteControl()
		f = open("output.csv", "r")
		reader = csv.reader(f, delimiter=',')
		i = 0
		for row in reader:
			if i == 0:
				self.assertEqual(row, ['1', 'SBS'])
			elif i == 1:
				self.assertEqual(row, ['2', 'KBS'])
			else:
				self.assertEqual(row, ['3', 'JTBC'])
			i += 1

		f.close()

	

	
if __name__ == "__main__":
	unittest.main()




