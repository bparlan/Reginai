# Reginai

Designing an aritificial intelligence model based on genetic algorithm that will survive and thrive in real market.

## Current Mainstream Idea

develop a strategy to find fittest algorithm to buy and sell order placement which is mainly **buy at low and sell at high.**

## Genetic Alhorithms

*inspired by the notion of 'survival of the fittest' from Darwinian Evolution and modern genetics.*

### How does it work?

0. Initialisation
   *loop between 1-4*
1. Evaluate
2. Terminate?
3. Selection
4. Variation

### Example: Achivements of GA for a game:

> design ai behaviour with preference towards:
>   - fast level completion
>   - aggressiveness
>   - score achievement
>   - coins collected
>   - or compromise of the above

### Example: Evolution of Survival of the Fittest

genome population:

- long entry: cycle with length 20-100
- long exit: RSI(length, value)
- short entry: cycle with length 20-100
- short exit RSI(length, value)

fittest parameter:

- contant up-sloping equity curve [*actually wrong because adaptation may require understandable amount of loss and sacrafice, adaptation is not always winning, but lowering losses for survival*]
- highest System-Quality-Number SQN
- more trades = better (min. trades = 20) [*just, why?*]

## Reginai Aproach: Survival of the Adapter

But what if we agree that predicting future is impossible, and fittest to one event can be  and focus on just get ready to have a 'change' in any direction?

Each chromosome stores x different genes.

value to fit: wallet_size
success condition: highest wallet_size from an 'event' cycle.
    cycle start - end point
        when price stays in bollinger band middle, with 50 mfi and relatively average (or low) atr.

instincts: fear, greed

- [pump detector](https://github.com/RomanGorbatko/binance-pump-detector) / [whale watcher](https://github.com/uzillion/crypto-whale-watcher)

adaptations: which sensors to consider to determine behavior
event identification?
evolve sensors or behaviors?
behaviors:

map function to generate gradient of buy-sell order list from heatmap we develop.

## Technical Notes

Node.js / Python?
talib
genetic algorithm
binance
telegram
algotrading

## Roadmap

1. Communicate with Binance. [python](https://github.com/sammchardy/python-binance) / [node](https://github.com/bparlan/bitprophet)
2. ta-lib [node.talib](https://github.com/oransel/node-talib)
2. telegram bot (gerçekten deneme için bu gerekli, yoksa kafayı yiycem)
3. developing behaviour algorithms
4. genetic algorithm [python] / [node](https://github.com/sripberger/gene-lib)
5. webserver
