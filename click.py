### click.py
## 指定した時間に、左クリックをするプログラム
# -*- coding: utf-8 -*-

# モジュールのインポート
#　pyautogui：マウスの位置取得、クリックするためのモジュール
#　datetime：現在時刻の取得
import pyautogui as pa
from datetime import datetime

# 現在時刻の取得
now = datetime.now()
print(now) # 例　09:55:28

# # 指定の時間（start_hour）になるのを計測する
# start_hour = 6
# # 指定時間になるまで、現在時刻を”now”に更新する
# while now.hour < start_hour:
#     now = datetime.now()



# 指定の時間（start_min）になるのを計測する
start_min = 41
# 指定時間になるまで、現在時刻を”now”に更新する
while now.minute < start_min:
    now = datetime.now()

# 現在のマウス座標を取得する
x,y=pa.position()

# 指定したマウス座標でクリックさせる
# click(x座標、y座標、クリック回数、時間間隔、押すボタン)
pa.click(x, y, 1, 0.0, 'left')
print(now)
print(i)
