from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# 🔴 PUT YOUR BOT TOKEN HERE
BOT_TOKEN = "8251478689:AAGhvUp2YnrHe4ihSBtZZELOIxjbLDaawfw"

# 🔗 PUT YOUR TELEGRAM LINK HERE
MY_TELEGRAM_LINK = "https://t.me/karlou98"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome 👋\n\nHere are some photos 📸\n\nContact me:\n" + MY_TELEGRAM_LINK
    )

    photo_folder = "photos"

    for photo_name in os.listdir(photo_folder):
        photo_path = os.path.join(photo_folder, photo_name)
        with open(photo_path, "rb") as photo:
            await update.message.reply_photo(photo)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Type /start to see photos\n\nContact me:\n" + MY_TELEGRAM_LINK
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
