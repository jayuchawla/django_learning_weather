from django.shortcuts import render
import os
import dotenv
import json
import requests
from pathlib import Path

ROOT_DIR=Path(__file__).resolve().parent.parent
# Add .env variables anywhere before SECRET_KEY
dotenv_file = os.path.join(ROOT_DIR, ".env.secret")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)
API_SECRET_KEY = os.environ['LOOKUP_API_SECRET_KEY']

# Create your views here.
def home(request):

    if request.method == "POST":
        zipcode = request.POST['zipcodeInput']
        if zipcode:
            REMOTE_API = 'https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode={}&date=2023-04-29&distance=5&API_KEY={}'.format(zipcode, API_SECRET_KEY)
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