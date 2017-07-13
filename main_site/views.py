from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'main_site/home.html')


def contact(request):
  return render(request, 'main_site/basic.html', 
          {'content':['Work in progress. Look around. Help if you can.']})

