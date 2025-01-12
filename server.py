from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '7634693292:AAG0R0BzpJkPrva769oeVcFHhPnbEDjw9zE'  # Замените на токен вашего бота
CHAT_ID = '-1002498883253'  # Замените на ID канала или пользователя

@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form.get('name')
    telegram = request.form.get('telegram')
    message = request.form.get('message')

    text = f"💬 Новое сообщение с сайта:\n👤 Имя: {name}\n📱 Telegram: {telegram}\n✉️ Сообщение: {message}"

    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': text}

    response = requests.post(url, data=data)

    if response.status_code == 200:
        return 'Сообщение отправлено в Telegram!'
    else:
        return 'Ошибка при отправке сообщения.', 500

if __name__ == '__main__':
    app.run(port=3000)
