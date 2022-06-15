class Tester(unittest.TestCase):
	def test_getNewinteger(self):
		t = IntegerAccumulator()
		self.assertEqual(t.getNewInteger(0),0)
		self.assertEqual(t.getNewInteger(2),1)
		self.assertEqual(t.getNewInteger(4),2)

	def test_getAccumulatedIntegers(self):
		t = IntegerAccumulator()
		t.getNewInteger(5)
		t.getNewInteger(3)
		t.getNewInteger(4)
		self.assertEqual(t.getAccumulatedIntegers(),[5, 3, 4])

	def test_getAverage(self):
		t = IntegerAccumulator()
		for i in range(1, 101):
			t.getNewInteger(i)
		self.assertEqual(t.getAverage(),50)

if __name__ == "__main__":
	unittest.main()
