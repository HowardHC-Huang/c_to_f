##攝氏轉換成華氏程式
#(解答→ 建立github專案+上傳→ 更新readme檔)


#[重要!]思考架構:
#使用者輸入 攝氏
#印出華氏

celsius = float(input('請輸入攝氏溫度:'))
fahrenheit = celsius * 9 / 5 + 32
print('等於華氏', fahrenheit, '度')