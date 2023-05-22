from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')






@app.route('/count_characters', methods=['POST'])
def count_characters():
    text = request.form['text']
    count = len(text)
    return render_template('index.html', count=count)

if __name__ == '__main__':
    app.run()
    
    
import requests
@app.route('/geocode',method=['POST'])
def geocode():
    # Geocoding APIのURL
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    text = request.form['text1']
    # パラメータを設定
    params = {
        "address": text,
        "key": "AIzaSyA9LVCO3v_Qd8D5rFA04-JtxyAs-u1jdeI"  # 自分のAPIキー
    }

    # リクエストを送信
    response = requests.get(url, params=params)
    
    # レスポンスのJSONデータを取得
    data = response.json()

    # 結果を表示
    if data["status"] == "OK":
        # 最初の結果の緯度と経度を取得
        result = data["results"][0]
        location = result["geometry"]["location"]
        lat = location["lat"]
        lng = location["lng"]
        #print("緯度:", lat)
        #print("経度:", lng)
    else:
        #print("エラー:", data["status"])
    return render_template('index.html', lat=lat)

if __name__ == '__main__':
    app.run()

# 例として東京タワーの住所を指定してgeocode関数を呼び出す
#geocode("東京都港区芝公園４丁目２−８")
