import pandas as pd
x = pd.read_json('data.json')
print(x.to_string())

import pandas as pd 
data = {
    {
    "Duration": 96,
    "Pulse": 67,
    "Maxpulse": 123,
    "Calories": 581.6
  },
  {
    "Duration": 50,
    "Pulse": 75,
    "Maxpulse": 148,
    "Calories": 332
  },
  {
    "Duration": 109,
    "Pulse": 66,
    "Maxpulse": 189,
    "Calories": 1301.7
  },
  {
    "Duration": 90,
    "Pulse": 87,
    "Maxpulse": 124,
    "Calories": 286
  },
  {
    "Duration": 26,
    "Pulse": 73,
    "Maxpulse": 149,
    "Calories": 211.6
  }
}

x = pd.DataFrame(data)
print(x)