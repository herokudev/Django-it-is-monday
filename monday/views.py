import datetime

from django.shortcuts import render

# Create your views here.
def index(request):
  now = datetime.datetime.now()
  return render(request, 'ismonday.html', {'dayofweek': now.today().weekday() == 0})
