from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import BOT_TOKEN, CHANNEL_USERNAME
from fetch_sofascore import fetch_live_tennis_matches
import asyncio
import random

sent_ids = set()

betting_phrases = [
    "🔥 Hot Pick!",
    "🎯 Sharp Bet!",
    "⚡ Quick Tip!",
    "💸 Smart Move!",
    "🧠 Expert Insight!",
    "📈 Trending Now!",
    "✅ Safe Bet!",
    "🤑 Value Pick!"
]

async def post_live_matches(app):
    matches = fetch_live_tennis_matches()
    for match in matches:
        if match['id'] not in sent_ids:
            phrase = random.choice(betting_phrases)
            msg = f"🎾 {match['tournament']} – {match['match']}\n📊 Status: {match['score']}\n{phrase}"
            await app.bot.send_message(chat_id=CHANNEL_USERNAME, text=msg)
            sent_ids.add(match['id'])

async def scheduler(app):
    while True:
        await post_live_matches(app)
        await asyncio.sleep(60)

async def test_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is working! This is a test command response.")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("test", test_command))
    asyncio.create_task(scheduler(app))
    print("🤖 Bot is running with /test command...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
