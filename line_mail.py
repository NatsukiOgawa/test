#全てをまとめて、時報になるように、送る内容をtime（その時の時刻）にする
import requests
import datetime

time = datetime.datetime.now()
time = time.strftime('%Y年%m月%d日 %H:%M:%S')

TOKEN = 'ubh9DRuV9zdbxHuY7bRdyigA1nSVTaMj1O8E2oE9QJt'
api_url = 'https://notify-api.line.me/api/notify'
#時刻を送る内容の変数に設定
send_contents = time

TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
send_dic = {'message': send_contents}

image_file = './test.png'
binary = open(image_file, mode='rb')
image_dic = {'imageFile': binary}

requests.post(api_url, headers=TOKEN_dic, data=send_dic, files=image_dic)
