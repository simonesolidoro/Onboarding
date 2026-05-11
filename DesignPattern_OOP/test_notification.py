import unittest
from NotificationFactory import *

class TestNotificationFactory(unittest.TestCase):
    def test_email_notification(self):
        factory = NotificationFactory()
        notify = factory.notifycation_factory(param="SMS")
        self.assertEqual("SMSNotification", notify.send("",""))  # add assertion here


if __name__ == '__main__':
    unittest.main()
