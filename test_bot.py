from telegram import Bot
from config import BOT_TOKEN, CHANNEL_USERNAME

bot = Bot(token=BOT_TOKEN)

def send_test_message():
    try:
        test_message = "✅ Test message sent from Sofascore Tennis Bot!
This confirms your bot is working perfectly 🔥"
        bot.send_message(chat_id=CHANNEL_USERNAME, text=test_message)
        print("✅ Test message sent successfully.")
    except Exception as e:
        print("❌ Failed to send test message:", e)

if __name__ == "__main__":
    send_test_message()
