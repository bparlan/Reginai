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

### Why Node.js or Python?

Cengiz knows.

### Why Telegram and Binance?

Just because practicality of development. I already have an account on binance, and Telegram BotFather rocks.

### Genetic Algorithm

*Resource and more to read: [Investopedia](https://www.investopedia.com/articles/financial-theory/11/using-genetic-algorithms-forecast-financial-markets.asp)*

Trading rule parameters data is a one-dimensional vector, with direction and magnitude.
each vector is a chromosome, each parameter is a gene. parameter's considered values (genes) are modified by natural selection.

**[neuroevolution](https://www.mql5.com/en/articles/2225)** — similar to genetic programming, but genomes are artificial neural networks where evolution of weights at the specified network topology occurs, or besides evolution of weights topology evolution is also carried out.).

#### Genetik Operations

- crossover: Two-point crossing over
- mutation
- selection

#### Steps (loop)

1. Initialize a random population, where each chromosome is n-length, with n being the number of parameters. That is, a random number of parameters are established with n elements each.
2. Select the chromosomes, or parameters, that increase desirable results (presumably net profit).
3. Apply mutation or crossover operators to the selected parents and generate an offspring.
4. Recombine the offspring and the current population to form a new population with the selection operator.

#### Algobots

Financial life: have an income, expenses to pay, die when money goes 0.
Make Decision: buy, sell, nothing.
execute: time interval or event detection.

co-domination



Each chromosome stores x different genes.

value to fit: wallet_size
success condition: highest wallet_size from an 'event' cycle.
    cycle start - end point
        when price stays in bollinger band middle, with 50 mfi and relatively average (or low) atr.

instincts: fear, greed

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
2. ta-lib. [node.talib](https://github.com/oransel/node-talib)
3. telegram bot (for the sake of my insanity).
4. developing behaviour algorithms.
5. genetic algorithm. [python] / [node](https://github.com/sripberger/gene-lib)
6. webserver.

### Far Future

Instincts as genes:

- News Based Trading - Twitter data & StochAI
- [pump detector](https://github.com/RomanGorbatko/binance-pump-detector) / [whale watcher](https://github.com/uzillion/crypto-whale-watcher)

## Worth to mention

- Thanks to Anas Ameziane from [Ozzo](https://www.ozzo.io) for being there.
- The article.
- [Self-optimization of EA: Evolutionary and Genetic Algorithms](https://www.mql5.com/en/articles/2225) by Vladimir Perervenko.
