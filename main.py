# weather app
import requests
city = input("enter city name: ")
id = "44ed928f822db0c2d4b6f51e1cff94bf"
coord_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={id}"
def procesing():
    response1 = requests.get(coord_url)
    if response1.status_code == 200:
        print("response sent successfully")
        coord = response1.json()
        lon = coord[0]["lon"]
        lat = coord[0]["lat"]
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={id}"
        response2 = requests.get(url)
        if response2.status_code == 200:
            weather = response2.json()
            #print(weather)
            print(f"the temperature in {city}: {weather["main"]["temp"]}C")
            print(f"the min temperature in {city}: {weather["main"]["temp_min"]}C")
            print(f"the max temperature in {city}: {weather["main"]["temp_max"]}C")
        else:
            print("sumthing wrong!")
            print(response2)
    else:
        print("sumthing wrong!")
        print(response1)
try:
    procesing()
except Exception:
    print(f"error: {i}")
