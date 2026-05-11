class Notification:
    name = "Notification"
    def send(self,message: str, recipient: str):
        return self.name

class EmailNotification(Notification):
    name = "EmailNotification"
    pass
class SMSNotification(Notification):
    name = "SMSNotification"
    pass
class PushNotification(Notification):
    name = "PushNotification"
    pass

class NotificationFactory:
    def notifycation_factory(self, param : str):
        if not param in ["Email","SMS","Push"]:
            raise ValueError("param value not supported")
        if param == "Email":
            return EmailNotification()
        elif param == "SMS":
            return SMSNotification()
        elif param == "Push":
            return PushNotification()
    pass

