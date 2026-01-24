import json
import os

class OptOutManager:
    def __init__(self, storage_file="opt_out_list.json"):
        self.storage_file = storage_file
        self.opt_out_list = self._load_list()

    def _load_list(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as f:
                return set(json.load(f))
        return set()

    def _save_list(self):
        with open(self.storage_file, 'w') as f:
            json.dump(list(self.opt_out_list), f)

    def add_user(self, phone_number):
        self.opt_out_list.add(phone_number)
        self._save_list()

    def is_opted_out(self, phone_number):
        return phone_number in self.opt_out_list

    def check_message_for_opt_out(self, phone_number, message_text):
        # Hebrew "הסר" and English "Stop"
        trigger_words = ["הסר", "stop", "unsubscribe", "remove"]
        cleaned_text = message_text.strip().lower()
        if any(word in cleaned_text for word in trigger_words):
            self.add_user(phone_number)
            return True
        return False
