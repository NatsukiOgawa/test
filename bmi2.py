import tkinter as tk
#全てをまとめて、時報になるように、送る内容をtime（その時の時刻）にする
import requests
import datetime

# ボタンを押したときの処理 --- (*1)
def calc_bmi():

    time = datetime.datetime.now()   # 日付を取得する
    time = time.strftime('%Y年%m月%d日 %H:%M:%S')   # 見やすく変換する

    TOKEN = 'ubh9DRuV9zdbxHuY7bRdyigA1nSVTaMj1O8E2oE9QJt'
    api_url = 'https://notify-api.line.me/api/notify'
    #時刻を送る内容の変数に設定
    # send_contents = time
    send_contents = "プログラムが起動されました。"

    TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
    send_dic = {'message': send_contents}

    image_file = './test.png'
    binary = open(image_file, mode='rb')
    image_dic = {'imageFile': binary}

    requests.post(api_url, headers=TOKEN_dic, data=send_dic)


# ウィンドウを作成 --- (*2)
win = tk.Tk()
win.title("肥満判定")
win.geometry("500x250")

# 部品を作成 --- (*3)

calcButton = tk.Button(win, text=u'計算')
calcButton["command"] = calc_bmi
calcButton.pack()

# ウィンドウを動かす
win.mainloop()
