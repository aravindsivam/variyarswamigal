# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the Variyar Swamigal.com index.")

def home(request):
    return HttpResponse("This is the home page")
    
def gallery(request):
    return HttpResponse("This is the gallery page")

def books(request):
    return HttpResponse("This is the books page")

def  acds(request):
    return HttpResponse("This is the acds page")
