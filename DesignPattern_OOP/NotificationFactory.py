class Notification:
    def send(self,message: str, recipient: str):
        pass

class EmailNotification(Notification):
    pass
class SMSNotification(Notification):
    pass
class PushNotification(Notification):
    pass

class NotificationFactory:
    def notifycationFactory(self,param):
        if(param == 0):
            return EmailNotification()
        elif(param == 1):
            return SMSNotification()
        else:
            return PushNotification()
    pass

