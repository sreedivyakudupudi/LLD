
from abc import ABC, abstractmethod


# 1. Product Interface
class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


# 2. Concrete Products
class EmailNotification(Notification):

    def send(self, message):
        print(f"Sending Email: {message}")


class SMSNotification(Notification):

    def send(self, message):
        print(f"Sending SMS: {message}")


class PushNotification(Notification):

    def send(self, message):
        print(f"Sending Push Notification: {message}")


class WhatsAppNotification(Notification):

    def send(self, message):
        print(f"Sending WhatsApp: {message}")


# 3. Abstract Creator
class NotificationCreator(ABC):

    @abstractmethod
    def create_notification(self):
        pass

    # Common business workflow
    def notify_user(self, message):

        print("Validating message...")

        notification = self.create_notification()

        print("Logging notification...")

        notification.send(message)


# 4. Concrete Creators
class EmailCreator(NotificationCreator):

    def create_notification(self):
        return EmailNotification()


class SMSCreator(NotificationCreator):

    def create_notification(self):
        return SMSNotification()


class PushCreator(NotificationCreator):

    def create_notification(self):
        return PushNotification()


class WhatsAppCreator(NotificationCreator):

    def create_notification(self):
        return WhatsAppNotification()


# 5. Client Code
def main():

    creator = EmailCreator()
    creator.notify_user("Your order has been shipped!")

    print("--------------------")

    creator = SMSCreator()
    creator.notify_user("Your OTP is 123456")

    print("--------------------")

    creator = PushCreator()
    creator.notify_user("You have a new message!")

    print("--------------------")

    creator = WhatsAppCreator()
    creator.notify_user("Hello! Welcome to our service.")


if __name__ == "__main__":
    main()
