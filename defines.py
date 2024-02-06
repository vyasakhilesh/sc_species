## coordinates
coordinates_dict = {
    'Gebirgsbäche im Sauerland': {'latitude': 51.1234, 'longitude': 8.5678},
    'Plankton der Werse bei Münster': {'latitude': 51.9876, 'longitude': 7.6543},
    'Ruhr': {'latitude': 51.4567, 'longitude': 7.8901},
    'Lippe': {'latitude': 51.2345, 'longitude': 8.9012},
    'Eder': {'latitude': 50.8765, 'longitude': 8.3456},
    'Salinen und Salzgräben im südlichen Gebiet': {'latitude': 50.5432, 'longitude': 8.7654},
    'desgl. im nördlichen Gebiet': {'latitude': 50.7890, 'longitude': 8.1234},
    'Plankton der Talsperren': {'latitude': 51.4321, 'longitude': 7.5432},
    'Plankton des Dortmund-Ems Kanals': {'latitude': 51.8765, 'longitude': 7.2109},
    'Teiche und Moor stellen ,“Kipshagen ”': {'latitude': 51.6543, 'longitude': 8.0987},
    'Seen, Weiher und Moorstellen ,“Heiliges Meer"': {'latitude': 52.3456, 'longitude': 7.8901},
    'Moore im Sauer und Münsterland': {'latitude': 51.2345, 'longitude': 7.5432},}


"""coordinates_dict_new = {
  "Eder": {
    "latitude": 51.166667,
    "longitude": 8.75
  },
  "Gebirgsbäche im Sauerland": {
    "latitude": 51.25,
    "longitude": 8.25
  },
  "Gebirgsbäche im Sauerland": {
    "latitude": 51.25,
    "longitude": 8.25
  },
  "Lippe": {
    "latitude": 51.583333,
    "longitude": 8.5
  },
  "Moore im Sauer und Münsterland": {
    "latitude": 51.75,
    "longitude": 7.5
  },
  "Moore im Sauer und Münsterland": {
    "latitude": 51.75,
    "longitude": 7.5
  },
  "Moore im Sauer und Münsterland": {
    "latitude": 51.75,
    "longitude": 7.5
  },
  "Moore im Sauer-und Miinsterland": {
    "latitude": 51.75,
    "longitude": 7.5
  },
  "Plankton der Talsperren": {
    "latitude": 51.5,
    "longitude": 8.5
  },
  "Plankton der Werse bei Münster": {
    "latitude": 51.966667,
    "longitude": 7.616667
  },
  "Plankton der Werse bei Münster": {
    "latitude": 51.966667,
    "longitude": 7.616667
  },
  "Plankton der Werse bei Münster": {
    "latitude": 51.966667,
    "longitude": 7.616667
  },
  "Plankton des Dortmund-Ems Kanals": {
    "latitude": 51.5,
    "longitude": 7.5
  },
  "Ruhr": {
    "latitude": 51.5,
    "longitude": 7.5
  },
  "Salinen und Salzgruben im südlichen Gebiet": {
    "latitude": 51.5,
    "longitude": 8.5
  },
  "Salinen und Salzgruben im südlichen Gebiet": {
    "latitude": 51.5,
    "longitude": 8.5
  },
  "Salinen und Salzgräben im südlichen Gebiet": {
    "latitude": 51.5,
    "longitude": 8.5
  },
  "Seen, Weiher und Moorstellen , Heiliges Meer": {
    "latitude": 51.5,
    "longitude": 8.5
  },
  "Seen, Weiher und Moorstellen , Heiliges Meer": {
    "latitude": 51.5,
    "longitude": 8.5
  },
  "Teiche und Moor stellen , Kipshagen": {
    "latitude": 51.5,
    "longitude": 8.5
  },
  "Teiche und Moor stellen , Kipshagen": {
    "latitude": 51.5,
    "longitude": 8.5
  },
  "Teiche und Moor stellen ,“Kipshagen ”": {
    "latitude": 51.5,
    "longitude": 8.5
  },
  "Unnamed: 13": {
    "latitude": 51.5,
    "longitude": 8.5
  },
  "desgl. im n rdlichen Gebiet": {
    "latitude": 51.5,
    "longitude": 8.5
  },
  "desgl. im nrdlichen Gebiet": {
    "latitude": 51.5,
    "longitude": 8.5
  },
  "desgl. im nördlichen Gebiet": {
    "latitude": 51.5,
    "longitude": 8.5
  }
}"""


"""import googlemaps

client = googlemaps.Client(api_key="YOUR_API_KEY")

locations = [
    "Eder",
    "Gebirgsbäche im Sauerland",
    "Gebirgsbäche im Sauerland",
    "Lippe",
    "Moore im Sauer und Münsterland",
    "Moore im Sauer und Mnsterland",
    "Moore im Sauer und Münsterland",
    "Moore im Sauer-und Miinsterland",
    "Plankton der Talsperren",
    "Plankton der Werse bei M??nster",
    "Plankton der Werse bei Mnster",
    "Plankton der Werse bei Münster",
    "Plankton des Dortmund-Ems Kanals",
    "Ruhr",
    "Salinen und Salzgruben im s dlichen Gebiet",
    "Salinen und Salzgruben im s??dlichen Gebiet",
    "Salinen und Salzgräben im südlichen Gebiet",
    "Seen, Weiher und Moorstellen , Heiliges Meer",
    "Seen, Weiher und Moorstellen , Heiliges Meer",
    "Seen, Weiher und Moorstellen ,“Heiliges Meer”",
    "Teiche und Moor stellen , Kipshagen",
    "Teiche und Moor stellen ,??Kipshagen",
    "Teiche und Moor stellen ,“Kipshagen ”",
    "Unnamed: 13",
    "desgl. im n rdlichen Gebiet",
    "desgl. im nrdlichen Gebiet",
    "desgl. im nördlichen Gebiet",
]

results = []

for location in locations:
    geocode_result = client.geocode(location)

    latitude = geocode_result[0]["geometry"]["location"]["lat"]
    longitude = geocode_result[0]["geometry"]["location"]["lng"]

    results.append({"location": {"latitude": latitude, "longitude": longitude}})

print(results)"""
