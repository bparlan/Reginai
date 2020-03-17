'''

Behaviour 01
Looking for positions in safe waters.
req. low position_size and low risk_factor

1. Load 15m chart's volume.
2. if last_candle_volume <= average(lowest 4 candles of last 24 candle).
3. last_bollinger_range = find last bollinger band bubble & assign expansions total range between highest and lowest band.
4. place 20 sell_orders with amount of 0.02 each equally distributed* between current_price and current_price + last_bollinger_range
5. place 20 buy_orders with amount of 0.02 each equally distributed* between current_price and current_price - last_bollinger_range

* in future those will be not equally distributed, distribution will be with gradient weighted, including both location and amount.

'''