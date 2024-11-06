from flask import Flask, render_template, request
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

# Fungsi untuk mendapatkan data cuaca real-time dari API
def get_weather():
    # Ganti API_KEY dengan API key yang valid dari penyedia layanan cuaca (misalnya OpenWeatherMap)
    API_KEY = '3fb46824d347b47557232b8cd462c5b8'
    city = 'sambelia'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    
    # Cek apakah respons JSON memiliki kunci 'main' dan 'weather'
    if 'main' in data and 'weather' in data:
        weather = {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return weather
    else:
        # Jika respons JSON tidak sesuai dengan yang diharapkan, cetak data untuk debugging
        print("Unexpected JSON structure:")
        print(data)
        return None
    
# Halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Halaman tentang
@app.route('/teknik_pertanian')
def teknik_pertanian():
    return render_template('teknik_pertanian.html')

# Halaman harga pasar
@app.route('/harga_pasar')
def harga_pasar():
    return render_template('harga_pasar.html')

# Halaman bibit tanaman
@app.route('/bibit')
def bibit():
    return render_template('bibit.html')

# Halaman bibit tanaman
@app.route('/pupuk')
def pupuk():
    return render_template('pupuk.html')

# Halaman tampilan cuaca
@app.route('/weather')
def weather():
    weather_data = get_weather()
    if weather_data:
        return render_template('weather.html', weather=weather_data)
    else:
        return "Failed to retrieve weather data. Please check the server logs for more information."

if __name__ == '__main__':
    app.run(debug=True)