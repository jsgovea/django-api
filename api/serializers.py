from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse


def serialize_planet(planet):
    """
    Serialize a planet object to a dictionary that can be converted to JSON
    """
    return {
        "id": planet.id,
        "name": planet.name,
        "population": planet.population,
        "terrain": planet.terrain,
        "climate": planet.climate,
    }


def serialize_planets(planets):
    return [serialize_planet(planet) for planet in planets]
