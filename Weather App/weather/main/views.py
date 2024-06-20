from django.shortcuts import render
import json
import urllib.request

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        
        # Use your own API key here
        api_key = "a803ac641d4ee124aa458545d8c7fa5d"
        
        # Properly format the URL
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        
        # Make the request to the API
        try:
            source = urllib.request.urlopen(url).read()
            # Converting JSON data to a dictionary
            list_of_data = json.loads(source)
            
            # Data for variable list_of_data
            data = {
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": f"{list_of_data['coord']['lon']} {list_of_data['coord']['lat']}",
                "temp": str(list_of_data['main']['temp']) + 'k',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
            }
        except Exception as e:
            # Handle errors, such as city not found or API request issues
            print(e)
            data = {"error": "City not found or API request failed"}
    else:
        data = {}
    
    return render(request, "index.html", data)
