from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello world!')

# Create your views here.
