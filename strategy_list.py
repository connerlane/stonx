from sourcing_strats.tradeview import TopMovers, MostVolatile
from buying_strats.dumb import RandomBuy
from selling_strats.trailing_stop import TrailingStop
from strategy import Strategy


BASIC_STRATEGY = Strategy(
    "BASIC",
    [
        MostVolatile(),
    ],
    RandomBuy(),
    TrailingStop(),
)