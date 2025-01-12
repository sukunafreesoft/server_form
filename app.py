from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = '7634693292:AAG0R0BzpJkPrva769oeVcFHhPnbEDjw9zE'  # Замените на токен вашего бота
CHAT_ID = '-1002498883253'  # Замените на ID канала или пользователя

@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form.get('name')
    telegram = request.form.get('telegram')
    message = request.form.get('message')

    # Проверка на пустые поля
    if not name or not telegram or not message:
        return 'Ошибка: все поля должны быть заполнены.', 400

    text = f"💬 Новое сообщение с сайта:\n👤 Имя: {name}\n📱 Telegram: {telegram}\n✉️ Сообщение: {message}"

    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': text}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # Вызывает исключение, если статус-код 4xx или 5xx
    except requests.exceptions.RequestException as e:
        return f'Ошибка при отправке сообщения: {e}', 500

    return 'Сообщение отправлено в Telegram!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))  # Используйте переменную окружения PORT, если она есть
    app.run(host='0.0.0.0', port=port)
