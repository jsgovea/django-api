import json
import requests

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


from .forms import PlanetForm
from .helpers import parse_list
from .models import Planet
from .serializers import serialize_planet, serialize_planets

# Create your views here.


def swagger(request):
    return render(request, "index.html")


def get_query(request):
    response_data = {}
    url = "https://swapi-graphql.netlify.app/.netlify/functions/index"
    query = """
        query Query {
            allPlanets {
                planets {
                    name 
                    population 
                    terrains
                    climates
                    }
                }
            }
        """

    response = requests.post(url, json={"query": query})

    # Check if the response status code is 200 (success)
    if response.status_code == 200:

        # Convert the response to JSON for easy manipulation
        data = response.json()

        # Check if the data is not empty
        if data:

            # First we will start parsing the planets
            planets = data["data"]["allPlanets"]["planets"]

            # Loop through the planets and get the name, population, terrains and climates
            for planet in planets:
                planet_kwargs = {
                    "name": planet["name"],
                    "population": planet["population"] if planet["population"] else 0,
                    "terrain": parse_list(planet["terrains"]),
                    "climate": parse_list(planet["climates"]),
                }

                # Create a planet object
                Planet.objects.create(**planet_kwargs)
            response_data = planets

    return JsonResponse(response_data, safe=False)


# Added csrf_exempt for testing purposes, do not use in production
@csrf_exempt
def planet_list(request):
    response_data = {}

    # Check the request method
    if request.method == "GET":

        # Get the planets from the database
        planets = Planet.objects.all()
        response_data["planets"] = serialize_planets(planets)
        response_data["message"] = "Planets fetched successfully"
    elif request.method == "POST":
        data = json.loads(request.body)
        planet_form = PlanetForm(data)
        # Check if the form is valid
        if planet_form.is_valid():
            # Save the planet
            planet_form.save()
            response_data["message"] = "Planet created successfully"
            response_data["planet"] = serialize_planet(planet_form.instance)
        else:
            response_data["message"] = "An error occurred while creating the planet"
            response_data["errors"] = planet_form.errors
    return JsonResponse(response_data, content_type="application/json")


@csrf_exempt
def planet_detail(request, pk):
    response_data = {}

    # Get the planet from the database, using filter method to let us to use the exists() method
    planet = Planet.objects.filter(pk=pk)

    if planet.exists():
        if request.method == "GET":
            response_data["planet"] = serialize_planets(planet)
            response_data["message"] = "Planet fetched successfully"

        elif request.method == "PUT":
            data = json.loads(request.body)
            planet_data = {
                "name": data.get("name", planet[0].name),
                "population": data.get("population", planet[0].population),
                "terrain": data.get("terrain", planet[0].terrain),
                "climate": data.get("climate", planet[0].climate),
            }
            Planet.objects.filter(pk=pk).update(**planet_data)

            response_data["message"] = "Planet updated successfully"
            response_data["planet"] = serialize_planets(planet)

    else:
        response_data["message"] = "Planet does not exist. Try again."
    return JsonResponse(response_data, content_type="application/json")


@csrf_exempt
def delete_planet(request, pk):
    response_data = {}
    if request.method == "DELETE":
        planet = Planet.objects.filter(pk=pk)

        if planet.exists():
            planet.delete()
            response_data["message"] = "Planet deleted successfully"
        else:
            response_data["message"] = "Planet does not exist. Try again."
    return JsonResponse(response_data, content_type="application/json")
