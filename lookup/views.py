from django.shortcuts import render
import json
import requests

# Create your views here.
def home(request):

    if request.method == "POST":
        zipcode = request.POST['zipcodeInput']
        if zipcode:
            REMOTE_API = 'https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode={}&date=2023-04-29&distance=5&API_KEY=7CBBF8DD-2C91-42FD-A067-6758B85F8C17'.format(zipcode)
            response = None
            try:
                response = requests.get(REMOTE_API)
                data = json.loads(response.content)
                if len(data) > 0:
                    return render(request, 'home.html', {
                        'data': data, 
                        'categoryColorIdentifier': data[0]['Category']['Name'].replace(' ', '').lower
                    })
                else:
                    raise Exception('No results found...!')
            except Exception as e:
                # log
                print(e)
                return render(request, 'home.html', {'error': e})
        else:
            return render(request, 'home.html', {'error': 'Please enter a valid zipcode and try again!'})
    elif request.method == "GET":
        return render(request, 'home.html', {'error': 'Please enter a valid zipcode and try again!'})
    else:
        return render(request, 'home.html', {'error': 'Invalid Method...!'})

def about(request):
    return render(request, 'about.html', {})