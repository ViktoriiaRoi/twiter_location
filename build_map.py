'''
This module build map with location of user's friends
'''
import folium
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from geopy.exc import GeocoderUnavailable

geolocator = Nominatim(user_agent="main")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)


def find_coordinates(point: str) -> tuple:
    '''
    Find and return coordinates of place
    >>> find_coordinates('England, UK')
    (52.5310214, -1.2649062)
    >>> find_coordinates('Germany')
    (51.0834196, 10.4234469)
    '''
    try:
        location = geolocator.geocode(point)
        return (location.latitude, location.longitude)
    except (GeocoderUnavailable, AttributeError):
        return None


def build_map(coordinates:dict):
    '''
    Build map by users coordinates
    '''
    friends_marks = folium.FeatureGroup(name="Friends")

    for name in coordinates:
        lat, lon = coordinates[name]
        friends_marks.add_child(folium.Marker(location=[lat, lon], \
            popup=name, icon=folium.Icon(color='darkblue')))

    friends_map = folium.Map()
    friends_map.add_child(friends_marks)
    friends_map.add_child(folium.LayerControl())
    friends_map.save("templates/Friends_map.html")


def main(locations: dict):
    '''
    Build map with marks which represent location of user's friends
    '''
    coordinates = {}
    for key in locations:
        user_coord = find_coordinates(locations[key])
        if user_coord:
            coordinates[key] = user_coord
    build_map(coordinates)
