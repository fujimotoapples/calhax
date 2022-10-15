import requests
import json



test = requests.get("https://services.surfline.com/kbyg/spots/forecasts/wind?spotId=5842041f4e65fad6a77087f8")

wind_json = test.json()
#wind_dict = json.loads(wind_json)

print(type(wind_json))
print(wind_json['associated'])
# f = open("wind.json", "w")
# f.write(wind_json)
# f.close()

with open("wind.json", "w") as f:
    json.dump(wind_json, f)

    