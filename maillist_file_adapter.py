from maillist import MailList
import os, sqlite3


class MailListFileAdapter():
    """docstring for MailListFileAdapter"""
    def __init__(self, db_conn, mail_list=None):
        self.db_conn = db_conn
        self.mail_list = mail_list
        #self._ensure_db_path()
        self._ensure_db_exists()

    def get_file_name(self):
        return self.mail_list.get_name().replace(" ", "_")

    def get_file_path(self):
        return self.db_path + self.get_file_name()

    # (name, email) -> "<name> - <email>"
    def prepare_for_save(self):
        subscribers = self.mail_list.get_subscribers()
        subscribers = map(lambda t: "{} - {}".format(t[0], t[1]), subscribers)

        return sorted(subscribers)

    def _save_maillist(self):
        pass

    def _save_subscribers(self):
        pass

    def _save_relation(self, list_id, subscriber_id):
        pass

    def save(self):
        #file_to_save = open(self.get_file_path(), "w")
        #contents = "{}\n".format(self.mail_list.get_id())
        #contents += "\n".join(self.prepare_for_save())

        #file_to_save.write(contents)
        #file_to_save.close()

        _save_maillist()

        _save_subscribers()

    def load(self, file_name):
        maillist_name = file_name.replace("_", " ")

        # create a Dummy mail list, so we can call the methods
        if self.mail_list is None:
            self.mail_list = MailList(-1, maillist_name)

        file = open(self.get_file_path(), "r")
        contents = file.read()
        file.close()

        lines = contents.split("\n")
        maillist_id = int(lines[0])
        lines.pop(0)

        result = MailList(maillist_id, maillist_name)

        for unparsed_subscriber in lines:
            subscriber = unparsed_subscriber.split(" - ")
            result.add_subscriber(subscriber[0], subscriber[1])

        return result

    def _ensure_db_path(self):
        if not os.path.exists(self.db_path):
            os.makedirs(self.db_path)

