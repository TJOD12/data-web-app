from django.shortcuts import render
from django.http import HttpResponse
from .graphscripts import genline as gl

def home(request):
    return render(request, 'bogearrai/index.html')

def process_data(request):
    if request.method == "POST":
        county1 = request.POST.get("county1")
        county2 = request.POST.get("county2")
        county3 = request.POST.get("county3")

        requested_counties =  {
            "c1": county1,
            "c2": county2,
            "c3": county3,
        }

        graph = gl.generateGraph(requested_counties)

        context = {"graph": graph}

        return render(request, 'bogearrai/displayGraph.html', context)
    return render(request, 'bogearrai/displayGraph.html')