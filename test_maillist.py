import unittest
from maillist import MailList


class MailListTest(unittest.TestCase):
    """docstring for MailListTest"""

    def setUp(self):
        # fuck static
        self.m = MailList(1, "Hack Bulgaria")

    def test_create_mail_list_get_name(self):
        self.assertEqual("Hack Bulgaria", self.m.get_name())

    def test_add_subscriber(self):
        self.m.add_subscriber("Rado", "radorado@hackbulgaria.com")

        self.assertEqual(1, self.m.count())

    def test_get_subscribers(self):
        self.m.add_subscriber("Rado", "radorado@hackbulgaria.com")

        expected = [("Rado", "radorado@hackbulgaria.com")]
        actual = [(s.get_name(), s.get_email())
                for s in self.m.get_subscribers()]
        self.assertEqual(expected, actual)

    def test_get_id(self):
        self.assertEqual(1, self.m.get_id())

    def test_get_id_after_three_instances(self):
        m1 = MailList(1, "Hack")
        m2 = MailList(2, "Hack")
        m3 = MailList(3, "Hack")

        self.assertEqual(1, m1.get_id())
        self.assertEqual(2, m2.get_id())
        self.assertEqual(3, m3.get_id())

    def test_add_subscriber_with_same_email_address(self):
        subscriber_email = "radorado@hackbulgaria.com"

        add1 = self.m.add_subscriber("Rado", subscriber_email)
        add2 = self.m.add_subscriber("Rado Rado", subscriber_email)

        self.assertEqual(1, self.m.count())
        self.assertTrue(add1)
        self.assertFalse(add2)
        result = self.m.get_subscriber_by_email(subscriber_email)
        self.assertEqual(("Rado", subscriber_email),
                (result[0].get_name(), result[0].get_email()))

    def test_add_get_subscriber_by_email(self):
        self.m.add_subscriber("Rado", "radorado@hackbulgaria.com")

        result = self.m.get_subscriber_by_email("radorado@hackbulgaria.com")
        self.assertEqual(("Rado", "radorado@hackbulgaria.com"),
                (result[0].get_name(), result[0].get_email()))

    def test_add_get_subscriber_by_email_when_not_there(self):
        self.assertIsNone(self.m.get_subscriber_by_email("asd@asd.com"))

    def test_update_subscriber_changing_name(self):
        self.m.add_subscriber("Rado rado", "rado@rado.com")
        self.m.update_subscriber("rado@rado.com",
                                 {"name": "Radoslav Georgiev"})

        result = self.m.get_subscriber_by_email("rado@rado.com")
        self.assertEqual("Radoslav Georgiev",
                         result[0].get_name())

    def test_update_subscriber_changing_email(self):
        self.m.add_subscriber("Rado rado", "rado@rado.com")
        self.m.update_subscriber("rado@rado.com",
                                 {"email": "radorado@rado.com"})

        result = self.m.get_subscriber_by_email("radorado@rado.com")
        self.assertEqual(("Rado rado", "radorado@rado.com"),
                        (result[0].get_name(), result[0].get_email()))

    def test_update_subscriber_changing_name_and_email(self):
        self.m.add_subscriber("Rado rado", "rado@rado.com")
        self.m.update_subscriber("rado@rado.com",
                                 {"name": "Radoslav Georgiev",
                                  "email": "radorado@rado.com"})

        result = self.m.get_subscriber_by_email("radorado@rado.com")
        self.assertEqual(("Radoslav Georgiev", "radorado@rado.com"),
                         (result[0].get_name(), result[0].get_email()))

    def test_remove_subscriber(self):
        self.m.add_subscriber("Rado rado", "rado@rado.com")
        self.m.remove_subscriber("rado@rado.com")

        self.assertEqual(0, self.m.count())

    def test_remove_subscriber_when_not_there(self):
        self.assertIsNone(self.m.remove_subscriber("rado@radorado.com"))

if __name__ == '__main__':
    unittest.main()
