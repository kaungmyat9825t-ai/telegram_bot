import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Get token from Railway environment variable
BOT_TOKEN = os.getenv("8251478689:AAGhvUp2YnrHe4ihSBtZZELOIxjbLDaawfw")

if not BOT_TOKEN:
    # If token is missing, print a friendly message and exit
    print("Error: BOT_TOKEN is not set. Please add it in Railway Environment Variables.")
    exit(1)  # Exit gracefully instead of crashing

# ----- Handlers -----

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send main menu when /start is called"""
    keyboard = [
        [InlineKeyboardButton("Option 1", callback_data="option1")],
        [InlineKeyboardButton("Option 2", callback_data="option2")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome! Choose an option:", reply_markup=reply_markup)

async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle menu button clicks"""
    query = update.callback_query
    await query.answer()  # Acknowledge the button press

    if query.data == "option1":
        keyboard = [[InlineKeyboardButton("Back", callback_data="back")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("You selected Option 1 ✅", reply_markup=reply_markup)

    elif query.data == "option2":
        keyboard = [[InlineKeyboardButton("Back", callback_data="back")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("You selected Option 2 ✅", reply_markup=reply_markup)

    elif query.data == "back":
        # Return to main menu
        keyboard = [
            [InlineKeyboardButton("Option 1", callback_data="option1")],
            [InlineKeyboardButton("Option 2", callback_data="option2")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Welcome back! Choose an option:", reply_markup=reply_markup)

# ----- Main -----

def main():
    """Start the bot"""
    app = Application.builder().token(BOT_TOKEN).build()

    # Command handler
    app.add_handler(CommandHandler("start", start))

    # Button callback handler
    app.add_handler(CallbackQueryHandler(handle_menu))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
