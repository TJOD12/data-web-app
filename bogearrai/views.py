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

        graph, pop_list = gl.generateGraph(requested_counties)

        context = {"graph": graph,
                    "c1": {county1: pop_list["c1"]},
                    "c2": {county2: pop_list["c2"]},
                    "c3": {county3: pop_list["c3"]},
                    "popdata": pop_list 
                    }

        return render(request, 'bogearrai/displayGraph.html', context)
    return render(request, 'bogearrai/displayGraph.html')

# {% for row in popdata.values %}
#                         {% for item in row %}
#                             {% for val in item %}
#                                 {{ val }}
#                             {% endfor %}
#                         {% endfor %}
#                     {% endfor %}