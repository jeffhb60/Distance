# This class will take two physical addresses and provide data about the distance.  This particular implementation uses googleapis and will require a
# a Google API key that will need to connect to Google Maps API.  
import googlemaps
import os


class Distance:
    def __init__(self, orig, dest):
        self.gmaps = googlemaps.Client(key=os.environ.get('api_key'))
        self.origin = orig
        self.destination = dest
        self._directions = None
        self._get_directions()

    def _get_directions(self):
        try:
            self._directions = self.gmaps.directions(self.origin, self.destination, mode="driving")
        except Exception as e:
            self._directions = None

    def get_distance_in_meters(self):
        if self._directions:
            return self._directions[0]['legs'][0]['distance']['value']
        return None

    def get_distance_in_miles(self):
        distance_in_meters = self.get_distance_in_meters()
        if distance_in_meters:
            return distance_in_meters * 0.000621371  # Convert meters to miles
        return None

    def get_origin(self):
        return self.origin

    def get_destination(self):
        return self.destination

    def get_estimated_duration(self):
        if self._directions:
            return self._directions[0]['legs'][0]['duration']['value']
        return None

    def get_estimated_duration_in_minutes(self):
        duration_in_seconds = self.get_estimated_duration()
        if duration_in_seconds:
            return duration_in_seconds / 60
        return None

    def get_route_summary(self):
        if self._directions:
            return self._directions[0]['summary']
        return None


