BOT_API_TOKEN = '6282567193:AAFk8q0Hw3DNsBZD3C3LS0EDr6WCkmWp9EQ' #yout token
HOST = 'https://api.openweathermap.org'
WEATHER_API_KEY = '9b0e1af96e47e4f2422df8f32b7c65f3'

CURRENT_WEATHER_GET = HOST + '/data/2.5/weather?lat={lat}&lon={lon}&appid=' + WEATHER_API_KEY + '&units=metric'
FIVE_DAY_FORECAST_GET = HOST + 'data/2.5/forecast?lat={lat}&lon={lon}&appid=' + WEATHER_API_KEY + '&units=metric'
