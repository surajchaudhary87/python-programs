# Python Polymorphism
# Project: Notification System


class EmailNotification:
    def send(self, message):
        print(f"Email notification: {message}")


class SMSNotification:
    def send(self, message):
        print(f"SMS notification: {message}")


class PushNotification:
    def send(self, message):
        print(f"Push notification: {message}")


def send_notification(notification, message):
    """Send a message using the supplied notification object."""
    notification.send(message)


def main():
    # Create notification objects
    email = EmailNotification()
    sms = SMSNotification()
    push = PushNotification()

    # Use the same function with different object types
    send_notification(email, "Your order has been confirmed.")
    send_notification(sms, "Your OTP is 123456.")
    send_notification(push, "Your package is out for delivery.")


if __name__ == "__main__":
    main()
