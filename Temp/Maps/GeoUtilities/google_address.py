from GeoUtilities.location import Location
from GeoUtilities.utilities import haversine_distance


class GoogleGeocodingData(Location):

    def __init__(self, geocoding_data: dict) -> None:
        self.geocoding_data = geocoding_data
        self._default_idx = 0

    @property
    def results(self):
        return self.geocoding_data.get('results', None)

    @property
    def default_address(self):
        results_list = self.results
        if results_list:
            return GoogleAddress(results_list[self._default_idx])

    @property
    def status(self):
        if self.geocoding_data:
            return self.geocoding_data.get('status', None)

    def get_closest_result(self, coordinates: tuple):
        """
        Returns the closest GoogleAddress result to a (lat, lgn) coordinates set
        """
        results_list = self.results
        if len(results_list) == 1:
            return results_list[0]
        elif len(results_list) > 1:
            distance = []
            addresses = [(i, GoogleAddress(el)) for i, el in enumerate(results_list)]
            for i, address in addresses:
                lat_a, lng_a = coordinates
                lat_b, lng_b = address.get_coordinates()
                dist = haversine_distance(lat_a, lng_a, lat_b, lng_b)
                distance.append((dist, GoogleAddress))
            retval = sorted(distance, key=lambda item: item[0])
            return retval[0][0]

    def get_info(self):
        return {"status": self.status, "results": self.results}

    def __repr__(self):
        return f'GoogleGeocodingData({self.geocoding_data})'

    def __len__(self):
        result_list = self.results
        if result_list:
            return len(result_list)
        return 0


class GoogleAddress(Location):

    def __init__(self, geocoding_data: dict) -> None:
        self.geocoding_data = geocoding_data

    @property
    def coordinates(self):
        return self.geocoding_data.get('geometry', None).get('location', None)

    @property
    def formatted_address(self):
        return self.geocoding_data.get('formatted_address', None)

    @property
    def address_components(self):
        retval = dict()
        address_data = self.geocoding_data.get('address_components', None)
        for el in address_data:
            el_type = el.get('types', None)
            if el_type:
                retval[el_type[0]] = el.get('long_name', None)
        return retval

    def get_info(self):
        retval = {
            'location': self.coordinates,
            'formatted_address': self.formatted_address,
            'address_components': self.address_components
        }
        return retval

    def __repr__(self):
        return f'GoogleAddress({self.geocoding_data})'

    def get_coordinates(self):
        if self.coordinates:
            return self.coordinates.get('lat'), self.coordinates.get('lng')

    def __len__(self):
        return len(self.address_components)

    # def __clean_up_results(self):
    #     results_list = self.results
    #     if results_list:
    #         if len(results_list) == 1:
    #             return [0]
    #
    #         results_components = []
    #         for i, res in enumerate(results_list):
    #             components = res.get('address_components', [])
    #             compset = set()
    #             for comp in components:
    #                 compset.add(f"{comp['types'][0]}:{comp['long_name']}")
    #             if len(compset) > 0:
    #                 add_it = True
    #                 for el in results_components:
    #                     el_set = el[1]
    #                     if compset.issubset(el_set):
    #                         add_it = False
    #                         break
    #                     if compset.issuperset(el_set):
    #                         results_components.remove(el)
    #                         break
    #                 if add_it:
    #                     results_components.append((i, compset))
    #
    #         return [el[0] for el in results_components]
    #     return [0]
    #
    # @property
    # def adjusted_results(self):
    #     if self.results:
    #         return [el for i, el in enumerate(self.results) if i in self.__adjusted_results]
