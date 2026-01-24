import os
from src.api.client import WhatsAppClient, WarmupManager
from src.safety.opt_out import OptOutManager

class WhatsAppService:
    def __init__(self):
        token = os.getenv("WHATSAPP_TOKEN")
        phone_id = os.getenv("WHATSAPP_PHONE_NUMBER_ID")
        
        if not token or not phone_id:
            raise ValueError("WHATSAPP_TOKEN and WHATSAPP_PHONE_NUMBER_ID must be set")
            
        self.client = WhatsAppClient(token, phone_id)
        self.warmup = WarmupManager()
        self.opt_out = OptOutManager()

    def send_safe_message(self, to, text):
        if self.opt_out.is_opted_out(to):
            print(f"Skipping {to}: User has opted out.")
            return False

        if not self.warmup.can_send():
            print("Daily warm-up limit reached. Try again tomorrow.")
            return False

        result = self.client.send_text_message(to, text)
        if result:
            self.warmup.record_send()
            return True
        return False

if __name__ == "__main__":
    # Example usage
    # service = WhatsAppService()
    # service.send_safe_message("1234567890", "Hello from Aviel.AI Safety Integration!")
    pass
