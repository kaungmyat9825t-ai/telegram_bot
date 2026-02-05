from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

# ==============================
# 🔴 INSERT YOUR DETAILS HERE
# ==============================
import os
BOT_TOKEN = os.getenv ("8251478689:AAGhvUp2YnrHe4ihSBtZZELOIxjbLDaawfw")
MY_TELEGRAM_LINK = "https://t.me/karlou98"
# ==============================

# ---------- MAIN MENU KEYBOARD ----------
def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("🎰 Casino Games", callback_data="casino")],
        [InlineKeyboardButton("💼 Our Services", callback_data="services")],
        [InlineKeyboardButton("📸 Gallery", callback_data="gallery")],
        [InlineKeyboardButton("📞 Contact Us", callback_data="contact")]
    ]
    return InlineKeyboardMarkup(keyboard)

# ---------- BACK BUTTON ----------
def back_keyboard():
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("⬅️ Back to Menu", callback_data="back")]]
    )

# ---------- /start ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to KM Online Games Service 🎉\n\nChoose a menu below 👇",
        reply_markup=main_menu_keyboard()
    )

# ---------- BUTTON HANDLER ----------
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat_id

    if query.data == "casino":
        await context.bot.send_message(
            chat_id=chat_id,
            text="🎰 Casino Games Available\n\n"
                 "• Batman Bonus 20%\n"
                 "• Buffalo 688 Bonus 20%\n"
                 "• Golden Hand Bonus 20%\n"
                 "• ibet789 Bonus 10%\n"
                 "• 555Mix Bonus",
            reply_markup=back_keyboard()
        )

    elif query.data == "services":
        await context.bot.send_message(
            chat_id=chat_id,
            text="💼 Our Services\n\n"
                 "✔ Fast Deposit & Withdraw\n"
                 "✔ 24/7 Support\n"
                 "✔Senior AKL Online Game Service\n"
                 "✔ Trusted Online Gaming",
            reply_markup=back_keyboard()
        )

    elif query.data == "gallery":
        await context.bot.send_message(
            chat_id=chat_id,
            text="📸 Gallery\n\nPhotos below 👇",
            reply_markup=back_keyboard()
        )

        photo_folder = "photos"
        if os.path.exists(photo_folder):
            for photo_name in os.listdir(photo_folder):
                with open(os.path.join(photo_folder, photo_name), "rb") as photo:
                    await context.bot.send_photo(chat_id=chat_id, photo=photo)

    elif query.data == "contact":
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"📞 Contact Me\n\nTelegram 👉 {MY_TELEGRAM_LINK}",
            reply_markup=back_keyboard()
        )

    elif query.data == "back":
        await context.bot.send_message(
            chat_id=chat_id,
            text="🏠 Main Menu\n\nChoose a menu below 👇",
            reply_markup=main_menu_keyboard()
        )
