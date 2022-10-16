import requests
import json
import pandas as pd
import numpy as np
'''
Jacks URL:
https://www.surfline.com/surf-report/jack-s/5842041f4e65fad6a770880b?camId=5834946f3421b20545c4b51a
    
'''
wind_request = requests.get("https://services.surfline.com/kbyg/spots/forecasts/wind?spotId=5842041f4e65fad6a770880b")
wind_json = wind.json()
with open("wind.json", "w") as f:
    json.dump(wind_json, f)

wind_df = pd.DataFrame(wind_json)


    