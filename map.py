


import requests

def geocode(address):
    # Geocoding APIのURL
    url = "https://maps.googleapis.com/maps/api/geocode/json"

    # パラメータを設定
    params = {
        "address": address,
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
        print("緯度:", lat)
        print("経度:", lng)
    else:
        print("エラー:", data["status"])

# 例として東京タワーの住所を指定してgeocode関数を呼び出す
#geocode("東京都港区芝公園４丁目２−８")

gecode()




def places_search(location, radius, keyword):
    # Places APIのURL
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    # パラメータを設定
    params = {
        "location": location,
        "radius": radius,
        "keyword": keyword,
        "key": "AIzaSyA9LVCO3v_Qd8D5rFA04-JtxyAs-u1jdeI"  # 自分のAPIキー
    }
    response = requests.get(url, params=params)

    # レスポンスのJSONデータを取得
    data = response.json()

    # 結果を表示
    if data["status"] == "OK":
        results = data["results"]
        for result in results:
            name = result["name"]
            address = result["vicinity"]
            print("名称:", name)
            print("住所:", address)
            print("",)
            #観光地の場所、名称、最寄りの駅やバス停、評価ランキング
            #print("----------")
    else:
        print("エラー:", data["status"])
# 例として東京タワー周辺のレストランを検索する
#places_search("35.658584,139.745431", 1000, "レストラン")  




def geocode1(address):
    # Geocoding APIのURL
    url = "https://maps.googleapis.com/maps/api/geocode/json"

    # パラメータを設定
    params = {
        "address": address,
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
        print("緯度:", lat)
        print("経度:", lng)
    else:
        print("エラー:", data["status"])
    
    

# 例として東京タワーの住所を指定してgeocode関数を呼び出す
#geocode1("東京都港区芝公園４丁目２−８")