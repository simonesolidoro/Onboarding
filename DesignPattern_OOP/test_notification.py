import pytest
from NotificationFactory import *

@pytest.fixture
def notification_factory():
    return NotificationFactory()

@pytest.mark.parametrize("type_not,expected",
                         [("SMS","SMSNotification"),
                          ("Email","EmailNotification"),
                          ("Push","PushNotification")])
def test_notification_factory(notification_factory,type_not ,expected ):
    notify = notification_factory.factory(param=type_not)
    assert expected == notify.send("","")  # add assertion here
def test_notification_factory_exception(notification_factory):
    with pytest.raises(ValueError):
        notify = notification_factory.factory(param="Whatsapp")
