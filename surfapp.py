from flask import Flask, render_template
from buoydatareader import *

app = Flask(__name__)



rincon_wave_data = Waves('https://www.ndbc.noaa.gov/data/realtime2/41115.txt')
rincon_wave_conditions = [rincon_wave_data.get_wave_heights(),
                           rincon_wave_data.get_wave_periods(),
                           rincon_wave_data.get_wave_direction()]

rincon_wind_data = Winds('https://www.ndbc.noaa.gov/data/realtime2/41115.txt')
rincon_wind_conditions = [rincon_wind_data.get_wind_speed(),
                           rincon_wind_data.get_gusts(),
                          rincon_wind_data.get_wind_direction()]

sanjuan_wave_data = Waves('https://www.ndbc.noaa.gov/data/realtime2/41053.txt')
sanjuan_wave_conditions = [sanjuan_wave_data.get_wave_heights(),
                           sanjuan_wave_data.get_wave_periods(),
                           sanjuan_wave_data.get_wave_direction()]

sanjuan_wind_data = Winds('https://www.ndbc.noaa.gov/data/realtime2/41053.txt')
sanjuan_wind_conditions = [sanjuan_wind_data.get_wind_speed(),
                           sanjuan_wind_data.get_gusts(),
                           sanjuan_wind_data.get_wind_direction()]


@app.route("/")
@app.route("/home")
@app.route("/rincon")
def home():
    return render_template('home.html',
                           rincon_wave_conditions=rincon_wave_conditions,
                           rincon_wind_conditions=rincon_wind_conditions)

@app.route("/sanjuan")
def sanjuan():
    return render_template('sanjuan.html',
                           sanjuan_wave_conditions=sanjuan_wave_conditions,
                           sanjuan_wind_conditions=sanjuan_wind_conditions)

if __name__ == '__main__':
    app.run(debug=True)


