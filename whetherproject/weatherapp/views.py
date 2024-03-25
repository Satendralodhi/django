from django.shortcuts import render,HttpResponse
import urllib.request
import json
# Create your views here.
def index(request):

    try:
        if request.method == 'POST':

            city = request.POST['city']

            source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&units=metric&appid=61a31c7db769dd56fc1dad3b00b31785').read()
            list_of_data = json.loads(source)

            data = {
                "city":str(city),
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ', '
                + str(list_of_data['coord']['lat']),

                "temp": str(list_of_data['main']['temp']) + ' °C',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                'main': str(list_of_data['weather'][0]['main']),
                'description': str(list_of_data['weather'][0]['description']),
                'icon': list_of_data['weather'][0]['icon'],
            }
            print(data)
        else:
            data = {}

        return render(request, "main/index.html", data)
    except:
        return HttpResponse('data is not found')