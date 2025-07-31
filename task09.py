class Notification:
    def send(self):
        return "Sending notification"

class EmailNotification(Notification):
    def send(self):
        return "Email sent to inbox"

class SMSNotification(Notification):
    def send(self):
        return "SMS sent to phone"

messages = [EmailNotification(), SMSNotification()]
for msg in messages:
    print(msg.send())