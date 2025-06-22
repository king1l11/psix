import telebot
import flask
import os

API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

bot = telebot.TeleBot(API_TOKEN)
app = flask.Flask(__name__)

# 📌 Устанавливаем webhook при запуске
bot.remove_webhook()
bot.set_webhook(url=f"{WEBHOOK_URL}/{API_TOKEN}")

@app.route(f"/{API_TOKEN}", methods=["POST"])
def webhook():
    json_str = flask.request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "", 200

@app.route("/")
def index():
    return "Бот работает!"

