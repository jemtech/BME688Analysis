import unittest
from data.entry import Entry

class EntryTestCase(unittest.TestCase):
    def setUp(self):
        self.entry = Entry(1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,0.0)
    
    def test_sqSum(self):
        self.assertEqual(round(self.entry.sqSum(), 3), (344.85),
                         'incorrect value')

if __name__ == '__main__':
    unittest.main()
