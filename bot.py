import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes


WEB_APP_URL = "https://piska0bobrika-rgb.github.io/hello_bot/"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "🌐 Открыть Mini App",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Hello World! 🌍\n\n"
        "Нажми кнопку ниже, чтобы открыть мини-приложение:",
        reply_markup=reply_markup
    )


def main():

    token = os.environ["BOT_TOKEN"]

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))

    print("Бот запущен!")

    app.run_polling()


if __name__ == "__main__":
    main()