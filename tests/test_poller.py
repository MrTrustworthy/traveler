
import unittest
import traveler


class MainTest(unittest.TestCase):

    def test_base(self):
        self.assertTrue(True)

    def setUp(self):
        self.poller = traveler.Poller()

    def test_poller(self):

        j = self.poller.load()
        self.assertTrue(isinstance(j, str))

if __name__ == '__main__':
    unittest.main()
