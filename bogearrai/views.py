from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'bogearrai/index.html')

def process_data(request):
    if request.method == "POST":
        county1 = request.POST.get("county1")
        county2 = request.POST.get("county2")
    return HttpResponse(f"You picked {county1} and {county2}")