
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Welcome to Jarvis AI Bot!

Send /signals to get your free demo forex and crypto signals.")

async def signals(update: Update, context: ContextTypes.DEFAULT_TYPE):
    demo_signals = """📊 Demo Trading Signals:

1. 🟢 Buy EUR/USD @ 1.0750 | SL: 1.0720 | TP: 1.0800
2. 🔴 Sell BTC/USDT @ 65500 | SL: 66100 | TP: 64500
3. 🟢 Buy ETH/USDT @ 3200 | SL: 3150 | TP: 3300
4. 🔴 Sell GBP/JPY @ 191.50 | SL: 192.10 | TP: 190.50
"""
    await update.message.reply_text(demo_signals)

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signals", signals))

    print("Bot is running...")
    app.run_polling()
