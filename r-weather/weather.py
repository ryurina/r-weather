from flask import Flask, url_for, render_template, request, redirect
import requests as r
import datetime
import time 

app = Flask(__name__)

# Get your api https://openweathermap.org/api
api_key = "YOUR_API_KEY_HERE"

x = datetime.datetime.now()

datetime_str = "{} {} {} {}".format(x.strftime("%a"), x.strftime("%d"), x.strftime("%b"), x.strftime("%Y"))

@app.route("/", methods=["GET", "POST"])
def weather():
	if request.method == "POST":
		city = request.form["city"]
		try:
			api_data = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)
			response = r.get(api_data).json()
			city_name = response["name"]
			temperature = int(response["main"]["temp"] - 273.15)
			icon = response["weather"][0]["icon"]
			weather_description = response["weather"][0]["description"]
			max_temp = int(response["main"]["temp_max"] - 273.15)
			min_temp = int(response["main"]["temp_min"] - 273.15)
			lat = response["coord"]["lat"]
			lon = response["coord"]["lon"]
			pressures = response["main"]["pressure"]
			humidity= response["main"]["humidity"]
			unixtime_sunrise = response["sys"]["sunrise"]
			sunrise = time.strftime("%H:%M", time.localtime(unixtime_sunrise))
			unixtime_sunset = response["sys"]["sunset"]
			sunset = time.strftime("%H:%M", time.localtime(unixtime_sunset))
			return render_template("weather.html", city_name=city_name, icon=icon, temperature=temperature, weather_description=weather_description, max_temp=max_temp, min_temp=min_temp, date_now=datetime_str, lon=lon, lat=lat, pressure=pressures, humidity=humidity, sunrise=sunrise, sunset=sunset)
		except KeyError:
			return redirect(url_for("weather"))
	else:
		user_city = "London"
		api_data = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(user_city, api_key)
		response = r.get(api_data).json()
		city_name = response["name"]
		temperature = int(response["main"]["temp"] - 273.15)
		icon = response["weather"][0]["icon"]
		weather_description = response["weather"][0]["description"]
		max_temp = int(response["main"]["temp_max"] - 273.15)
		min_temp = int(response["main"]["temp_min"] - 273.15)
		lat = response["coord"]["lat"]
		lon = response["coord"]["lon"]
		pressures = response["main"]["pressure"]
		humidity = response["main"]["humidity"]
		unixtime_sunrise = response["sys"]["sunrise"]
		sunrise = time.strftime("%H:%M", time.localtime(unixtime_sunrise))
		unixtime_sunset = response["sys"]["sunset"]
		sunset = time.strftime("%H:%M", time.localtime(unixtime_sunset))
		return render_template("weather.html", city_name=city_name, icon=icon, temperature=temperature, weather_description=weather_description, max_temp=max_temp, min_temp=min_temp, date_now=datetime_str, lon=lon, lat=lat, pressure=pressures, humidity=humidity, sunrise=sunrise, sunset=sunset)


if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")
