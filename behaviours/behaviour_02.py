'''

Behaviour 02
Looking for safe waters.
uses volume

1. [v] Load 15m chart's volume.
2. [v] if last_candle_volume <= average(lowest 5 candles of last 25 candle) then;
3. safe_water = % (normalized weight) (ex: if lowest candle then 1, if 4th lowest then .92

'''