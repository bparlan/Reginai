from binance.client import Client
import configparser
from telegram.ext import Updater, CommandHandler


def hello(update, context):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


config = configparser.ConfigParser()
config.read('config.ini')

updater = Updater(config['TELEGRAM']['TOKEN'], use_context=True)
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.start_polling()
updater.idle()

client = Client(config['BINANCE']['API_KEY'], config['BINANCE']['API_SECRET'])

# get market depth
depth = client.get_order_book(symbol='BNBBTC')

# place a test market buy order, to place an actual order use the create_order function
# order = client.create_test_order(
#     symbol='BNBBTC',
#     side=Client.SIDE_BUY,
#     type=Client.ORDER_TYPE_MARKET,
#     quantity=100)

# get all symbol prices
prices = client.get_all_tickers()


# # withdraw 100 ETH
# # check docs for assumptions around withdrawals
# from binance.exceptions import BinanceAPIException, BinanceWithdrawException
#
# try:
#     result = client.withdraw(
#         asset='ETH',
#         address='<eth_address>',
#         amount=100)
# except BinanceAPIException as e:
#     print(e)
# except BinanceWithdrawException as e:
#     print(e)
# else:
#     print("Success")
#
# # fetch list of withdrawals
# withdraws = client.get_withdraw_history()

# # fetch list of ETH withdrawals
# eth_withdraws = client.get_withdraw_history(asset='ETH')
#
# # get a deposit address for BTC
# address = client.get_deposit_address(asset='BTC')


# # start aggregated trade websocket for BNBBTC
def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)
    # do something


from binance.websockets import BinanceSocketManager

bm = BinanceSocketManager(client)
bm.start_aggtrade_socket('BNBBTC', process_message)
bm.start()

# get historical kline data from any date range

# fetch 1 minute klines for the last day up until now
klines = client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
