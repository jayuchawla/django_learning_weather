### Learning Django
1. Create a venv && venv\Scripts\activate
2. pip install django
3. django-admin startproject weather
4. move venv to weather
5. python manage.py startapp lookup
6. Append 'lookup' to INSTALLED_APPS list in weather.settings
7. Append path('lookup/', include('lookup.urls')) in weather.urls.urlpatterns
8. In lookup create a directory called as templates && create base.html
9. For each template create a respective view in lookup.views and an entry in lookup.urls
