import unittest
from readText import ReadText
from runTest import TestDemo

class TestList(unittest.TestCase):

    names = None

    def setUp(self):
        read = ReadText()
        self.names = read.getUserName()
    
    def tearDown(self):
        pass

    def test_01(self):
        for name in self.names:
            run = TestDemo(name)
            run.test1()


if __name__ == "__main__":
    unittest.main()
