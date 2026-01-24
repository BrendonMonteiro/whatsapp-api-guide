import requests
import json
import logging
from datetime import datetime, timedelta

class WhatsAppClient:
    def __init__(self, token, phone_number_id, version="v18.0"):
        self.base_url = f"https://graph.facebook.com/{version}/{phone_number_id}"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        self.logger = logging.getLogger(__name__)

    def send_text_message(self, to, text_body):
        payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": to,
            "type": "text",
            "text": {"body": text_body}
        }
        try:
            response = requests.post(
                f"{self.base_url}/messages",
                headers=self.headers,
                data=json.dumps(payload)
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error sending message: {e}")
            if e.response is not None:
                self.logger.error(f"Response: {e.response.text}")
            return None

class WarmupManager:
    def __init__(self, stats_file="warmup_stats.json"):
        self.stats_file = stats_file
        self.load_stats()

    def load_stats(self):
        try:
            with open(self.stats_file, 'r') as f:
                self.stats = json.load(f)
        except FileNotFoundError:
            self.stats = {
                "start_date": datetime.now().isoformat(),
                "daily_counts": {}
            }

    def save_stats(self):
        with open(self.stats_file, 'w') as f:
            json.dump(self.stats, f)

    def get_current_limit(self):
        start_date = datetime.fromisoformat(self.stats["start_date"])
        days_since_start = (datetime.now() - start_date).days
        weeks_since_start = days_since_start // 7
        
        # Limit logic: 20/day week 1, 50/day week 2, 100/day week 3+
        if weeks_since_start == 0:
            return 20
        elif weeks_since_start == 1:
            return 50
        else:
            return 100

    def can_send(self):
        today = datetime.now().date().isoformat()
        current_count = self.stats["daily_counts"].get(today, 0)
        return current_count < self.get_current_limit()

    def record_send(self):
        today = datetime.now().date().isoformat()
        self.stats["daily_counts"][today] = self.stats["daily_counts"].get(today, 0) + 1
        self.save_stats()
