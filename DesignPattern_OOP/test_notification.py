import unittest
import pytest
from NotificationFactory import *

class TestNotificationFactory():
    @pytest.mark.parametrize("type_not,expected",[("SMS","SMSNotification"),("Email","EmailNotification"),("Push","PushNotification")])
    def test_email_notification(self,type_not ,expected ):
        factory = NotificationFactory()
        notify = factory.notifycation_factory(param=type_not)
        assert expected == notify.send("","")  # add assertion here

if __name__ == '__main__':
    unittest.main()
