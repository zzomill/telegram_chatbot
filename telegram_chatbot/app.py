from flask import Flask, render_template, request
#(모듈명) (flask 안의 메소드)
from decouple import config
import requests

app = Flask(__name__)

token = config('TELEGRAM_VOT_TOKEN')
chat_id = config('CHAT_ID')

url = 'https://api.telegram.org/bot'

@app.route('/')
def hello():
    return "Hello Mirae"

# 메세지를 작성할 곳 
@app.route('/write')
def write():
    return render_template('write.html')

# 메세지 보낼 곳 
@app.route('/send')
def send():
    # write.html에서 받아온 정보를 가져온다 
    text = request.args.get("text")
    #주소로 요청을으로 바로 실행한다. requests이용 (sendMessage 메소드를 사용)
    requests.get(f'{url}{token}/sendMessage?chat_id={chat_id}&text={text}')
    return render_template('send.html')


if __name__=="__main__":
	app.run(debug=True)