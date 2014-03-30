import unittest
from subscriber import Subscriber


class SubscriberTest(unittest.TestCase):
    def setUp(self):
        self.subscriber = Subscriber('asd', 'asd@asd')

    def test_get_id(self):
        self.assertEqual(-1, self.subscriber.get_id())

    def test_get_name(self):
        self.assertEqual('asd', self.subscriber.get_name())

    def test_get_email(self):
        self.assertEqual('asd@asd', self.subscriber.get_email())

if __name__ == '__main__':
    unittest.main()
