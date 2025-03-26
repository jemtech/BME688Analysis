import unittest
from data.cluster import Cluster
from data.entry import Entry

class ClusterTestCase(unittest.TestCase):
    def setUp(self):
        self.entries = [Entry(1,0,0,0,0,0,0,0,0,0),Entry(0,2,0,0,0,0,0,0,0,0)]
        self.cluster = Cluster(self.entries, "Test cluster")
    
    def test_cosine(self):
        entry = Entry(0,0,1,0,0,0,0,0,0,0)
        self.assertEqual(self.cluster.cosine(entry), (0.0),
                         'incorrect value')
        entry = Entry(-1,-2,0,0,0,0,0,0,0,0)
        self.assertEqual(self.cluster.cosine(entry), (-1.0),
                         'incorrect value')
        entry = Entry(1,2,0,0,0,0,0,0,0,0)
        self.assertEqual(self.cluster.cosine(entry), (1.0),
                         'incorrect value')

if __name__ == '__main__':
    unittest.main()