import pyupbit
import time
import datetime

from pyupbit.quotation_api import get_current_price

access = ""          # 본인 값으로 변경
secret = ""          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)
 
while True:
    try:
        My_DOGE = upbit.get_balance("DOGE")
        My_KRW = upbit.get_balance("KRW")
        orderbook = pyupbit.get_orderbook("KRW-DOGE")[0]['orderbook_units'][0]
        Supreme_sell = int(orderbook['ask_price'])
        Supreme_buy = int(orderbook['bid_price'])
        
#         # if Supreme_sell >= 1000 and My_ripple >= 118.0:
#         #     print(upbit.sell_limit_order("KRW-XRP", int(orderbook['bid_price'])+10, 120))
#         #     print(My_ripple)
#         #     print(My_KRW)

#         # elif Supreme_sell >= 1000 and My_KRW >= 120000.0:
#         #     print(upbit.buy_limit_order("KRW-XRP", int(orderbook['ask_price'])-10, 120))
#         #     print(My_ripple)
#         #     print(My_KRW)
# # 아래 한계값은 1020이 마지노선 
        
#         if 800 > Supreme_sell > 600 and My_ripple >= 186.0:
#             print(upbit.sell_limit_order("KRW-XRP", int(orderbook['bid_price'])+5, 250))
#             print(My_ripple)
#             print(My_KRW)

#         elif 800 > Supreme_sell > 600 and My_KRW >= 150000.0:
#             print(upbit.buy_limit_order("KRW-XRP", int(orderbook['ask_price'])-5, 250))
#             print(My_ripple)
#             print(My_KRW)
# 각 호가는 700을 뺀값의 6의 배수, 706(제외), 712, 718,... 996(제외)
# 아랫구간에서 매수 주문을 하지 못한채 오는 30000원 이상의 kRW 은 윗구간에서 -6 내림 주문을 32개로만 내리기때문에 아랫구간에서 오해가 생길 수 있다 
# 원래 50개를 주문을 (아랫동네에서-) 해야하는데 32개만 주문하므로 잉여값이, 수익으로 오인될 수 있는 요지. 
# 그때그때 수익을 아래로 내려서 매수주문으로 넣는 방식으로 채택하므로, 그대로 진행하되, 하루 점검시간때 오더 갯수의 차이로 파훼.
        
#         elif 700 > Supreme_sell > 600 and My_ripple >= 48.0:
#             print(upbit.sell_limit_order("KRW-XRP", int(orderbook['bid_price'])+4, 50))
#             print(My_ripple)
#             print(My_KRW)

#         elif 700 > Supreme_sell > 600 and My_KRW >= 30000.0:
#             print(upbit.buy_limit_order("KRW-XRP", int(orderbook['ask_price'])-4, 50))
#             print(My_ripple)
#             print(My_KRW)
# # 각 호가는 4의 배수, 만약 이구간에서 32개있는 채 매도가 주문되지않으면 윗구간에서 내려온것-> 위로 올리면 됨  600과 700 제외
   
#         elif 600 > Supreme_sell > 300 and My_ripple >= 63.0:
#             print(upbit.sell_limit_order("KRW-XRP", int(orderbook['bid_price'])+3, 65))
#             print(My_ripple)
#             print(My_KRW)

#         elif 600 > Supreme_sell > 300 and My_KRW >= 19500.0:
#             print(upbit.buy_limit_order("KRW-XRP", int(orderbook['ask_price'])-3, 65))
#             print(My_ripple)
#             print(My_KRW)
# # 각 호가는 3의 배수, 마찬가지로 50개 있는 채 매도 주문 안되면 윗구간에서 내려온것 -> 위로 올리면 됨. 300과 600 제외 
# # 또한 KRW 이 구간내로 매수주문 안된채로 있단것은 반대로 올라온것 --> 내리면 됨. 어쨋든 목표는 잦은 매매   
        
        if 340 > Supreme_sell > 180 and My_DOGE >= 570.0:
            print(upbit.sell_limit_order("KRW-DOGE", int(orderbook['bid_price'])+2, 580))
            print(My_DOGE)
            print(My_KRW)

        elif 340 > Supreme_sell > 180 and My_KRW >= 110000.0:
            print(upbit.buy_limit_order("KRW-DOGE", int(orderbook['ask_price'])-2, 580))
            print(My_DOGE)
            print(My_KRW)
# # 각 호가는 2의 배수

#         elif 200 > Supreme_sell > 150 and My_ripple >= 198.0:
#             print(upbit.sell_limit_order("KRW-XRP", int(orderbook['bid_price'])+1, 200))
#             print(My_ripple)
#             print(My_KRW)

#         elif 200 > Supreme_sell > 150 and My_KRW >= 30000.0:
#             print(upbit.buy_limit_order("KRW-XRP", int(orderbook['ask_price'])-1, 200))
#             print(My_ripple)
#             print(My_KRW)
# 모든호가에 ...
    except:
        print("에러 발생")
    time.sleep(0.2)