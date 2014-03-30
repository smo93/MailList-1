from subscriber import Subscriber
class MailList():
    """docstring for MailList"""
    def __init__(self, list_id, name):
        self.__name = name
        self.__id = list_id
        self.subscribers = []

    def add_subscriber(self, name, email):
        if email in [subs.get_email() for subs in self.subscribers]:
            return False

        self.subscribers.append(Subscriber(name, email))
        return True

    def get_name(self):
        return self.__name

    def count(self):
        return len(self.subscribers)

    def get_subscriber_by_email(self, email):
        subscriber = [subs for subs in self.subscribers
                if subs.get_email() == email]
        if len(subscriber) != 0:
            return subscriber

        return None

    def get_subscribers(self):
        return self.subscribers

    def update_subscriber(self, email, update_hash):
        if "name" in update_hash:
            [s.update_subscriber(update_hash["name"], s.get_email())
                    for s in self.subscribers if s.get_email() == email]

        if "email" in update_hash:
            [s.update_subscriber(s.get_name(), update_hash["email"])
                    for s in self.subscribers if s.get_email() == email]


    def remove_subscriber(self, email):
        #if email in self.subscribers:
            #del self.subscribers[email]

        [self.subscribers.pop(i) for i in range(len(self.subscribers))
                if self.subscribers[i].get_email() == email]

        return None

    def get_id(self):
        return self.__id
