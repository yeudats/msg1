from flask import Flask, request
import requests
TOKEN = '7871293487:AAEI-73NZUgtLD264QoKJ-Vya4kbCWZnLOM'
URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
CHAT_ID = '395009331'
app = Flask(__name__)

@app.route('/')
def index():
    return 'הבוט רץ!'


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(force=True)
    print(data)
    if data and 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')
        response = {
            'chat_id': chat_id,
            'text': f'היי! קיבלתי: {text}'
        }
        requests.post(URL, json=response)
    return '', 200



if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))  # Render תגדיר PORT כסביבת סביבה
    app.run(host='0.0.0.0', port=port)
