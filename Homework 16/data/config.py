from dotenv import load_dotenv, dotenv_values

load_dotenv()
config = dotenv_values('.env')

API_TOKEN = config['API_TOKEN']


# links to api
CATS_LINK = 'https://api.thecatapi.com/v1/images/search'
EXCHANGE_LINK = 'https://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
JOKE_LINK = 'http://rzhunemogu.ru/RandJSON.aspx?CType=1'
BTC_LINK = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
RECEIPT_LINK = 'https://www.themealdb.com/api/json/v1/1/random.php'
KP_LINK = 'https://kinopoiskapiunofficial.tech/api/v2.2/films/top?type=TOP_250_BEST_FILMS&page=1'
