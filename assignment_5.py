import requests
import pandas as pd


params = {"latitude": 50.45, "longitude": 30.52, "hourly": ["temperature_2m", "wind_speed_10m"], "forecast_days": 7}

response = requests.get("https://api.open-meteo.com/v1/forecast", params=params)
data = response.json()

organized_data = { "Date&Time": data["hourly"]["time"],
    "Temperature (°C)": data["hourly"]["temperature_2m"],
    "Wind Speed (m/s)": data["hourly"]["wind_speed_10m"]}

df = pd.DataFrame(organized_data)

df_3_days = df.head(72)

min_temperature = df_3_days['Temperature (°C)'].min()
max_temperature = df_3_days['Temperature (°C)'].max()
mean_temperature = df_3_days['Temperature (°C)'].mean()

print(f"Мінімальна температура за насупні 3 дні: {min_temperature}")
print(f"Максимальна температура за наступні 3 дні: {max_temperature}")
print(f"Середня температура за наступні 3 дні: {mean_temperature}")

mean_wind_speed = df['Wind Speed (m/s)'].mean()

wind_above_avg = df[df['Wind Speed (m/s)']>mean_wind_speed]

days_wind_above_avg = len(wind_above_avg)

print(f"К-сть годин із швидкістю вітру вище середнього: {days_wind_above_avg}")

