#!/usr/bin/env python3
"""Observer design pattern example."""


class NewsSubject:
    """Manage and notify subscribed observers."""

    def __init__(self):
        self._observers = []

    def subscribe(self, observer, topics=None):
        """Subscribe an observer to selected topics."""
        self._observers.append((observer, topics))

    def unsubscribe(self, observer):
        """Remove an observer."""
        self._observers = [
            item for item in self._observers
            if item[0] is not observer
        ]

    def notify(self, topic, data):
        """Notify observers interested in the topic."""
        for observer, topics in list(self._observers):
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver:
    """Log news events."""

    def update(self, topic, data):
        """Print a log notification."""
        print("log:{}={}".format(topic, data))


class EmailObserver:
    """Send email news events."""

    def update(self, topic, data):
        """Print an email notification."""
        print("email:{}={}".format(topic, data))


class SmsObserver:
    """Send SMS news events."""

    def update(self, topic, data):
        """Print an SMS notification."""
        print("sms:{}={}".format(topic, data))


def main():
    """Run the observer example."""
    subject = NewsSubject()

    log = LogObserver()
    email = EmailObserver()
    sms = SmsObserver()

    subject.subscribe(log, topics={"sports", "breaking"})
    subject.subscribe(email)
    subject.subscribe(sms, topics={"breaking"})

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
