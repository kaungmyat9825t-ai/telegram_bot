import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

print("Bot file loaded")

BOT_TOKEN = os.getenv("8251478689:AAGhvUp2YnrHe4ihSBtZZELOIxjbLDaawfw")
print("BOT_TOKEN exists:", bool("8251478689:AAGhvUp2YnrHe4ihSBtZZELOIxjbLDaawfw"))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is alive 🚀")

def main():
    print("Creating application")
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Starting polling")
    app.run_polling()

if __name__ == "__main__":
    main()
