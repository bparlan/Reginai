'''

Behaviour 01
Looking for positions in safe waters.
uses bollinger band & atr
at: tight bollinger band, by looking last wide bb.
req: current_position_size < 0.2, risk_factor < 0.2, safe_water > 0.9

1. [bb] last_bollinger_range = find last bollinger band bubble & assign expansions total range between highest and lowest band.
2. calculate areas *
    sell_area = equally distribute 20 points between (begin from (current_price + atr(20)) to (current_price + last_bollinger_range)
    buy_area = equally distribute 20 points between (begin from (current_price - atr(20)) to (current_price - last_bollinger_range)
3. place sell_orders to sell_area.
4. place buy_orders to buy_area.

* in future those will be not equally distributed, area will be with gradient weighted, including both location and amount, and distribution will be held upon gradient.

'''