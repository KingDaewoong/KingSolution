import pyupbit
import time
import datetime

from pyupbit.quotation_api import get_current_price

access = ""          # 본인 값으로 변경
secret = ""          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)
 
while True:
    try:
        My_ripple = upbit.get_balance("XRP")
        My_KRW = upbit.get_balance("KRW")
        orderbook = pyupbit.get_orderbook("KRW-XRP")[0]['orderbook_units'][0]
        Supreme_sell = int(orderbook['ask_price'])
        Supreme_buy = int(orderbook['bid_price'])
        

        
        if 900 > Supreme_sell > 600 and My_ripple >= 290.0:
            print(upbit.sell_limit_order("KRW-XRP", int(orderbook['bid_price'])+4, 300))
            print(My_ripple)
            print(My_KRW)

        elif 900 > Supreme_sell > 600 and My_KRW >= 190000.0:
            print(upbit.buy_limit_order("KRW-XRP", int(orderbook['ask_price'])-4, 300))
            print(My_ripple)
            print(My_KRW)

    except:
        print("에러 발생")
    time.sleep(0.2)