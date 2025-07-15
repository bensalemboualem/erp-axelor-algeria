class TelegramAgent:
    def __init__(self, bot_token):
        self.bot_token = bot_token
        print("📱 Telegram Agent Algeria initialisé")
    
    async def send_message(self, chat_id, text):
        # Envoi message Telegram
        return f"📤 Telegram: {text[:50]}..."

class SignalAgent:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        print("🔐 Signal Agent Algeria initialisé")
    
    async def send_message(self, recipient, text):
        # Envoi message Signal
        return f"🔒 Signal: {text[:50]}..."

print("✅ Multi-Platform Agents ready!")
