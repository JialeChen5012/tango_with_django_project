

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# each view takes at least one HttpResponse object and returns one
def index(request):
# Construct a dictionary to pass to the template engine as its context.
# Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
# Return a rendered response to send to the client.
# We make use of the shortcut function to make our lives easier.
# Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("<a href='/rango/'>Index</a>Rango says here is the about page.")