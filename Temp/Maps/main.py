from map_points import MapPoint
from googe_geocoding import GeocodingAPI as gc

# kupenite_22 = MapPoint.from_coordinates(42.661954442677605, 23.268147364779765)
# kupenite_1 = MapPoint.from_coordinates(42.66297713687513, 23.26424424421194)

connector = gc('json')

kupenite_22 = MapPoint('София, ул. Купените 22')
coordinates = gc.extract_coordinates(connector.get_location_data(kupenite_22.address, region='BG'))
kupenite_22.latitude, kupenite_22.longitude = coordinates['lat'], coordinates['lng']

milkovitsa = MapPoint('с. Милковица, обл. Плевен')
coordinates = gc.extract_coordinates(connector.get_location_data(milkovitsa.address, region='BG'))
milkovitsa.latitude, milkovitsa.longitude = coordinates['lat'], coordinates['lng']

distance = kupenite_22.get_distance(milkovitsa)
print(distance)


# {'results':
#   [{'address_components':
#       [{
#           'long_name': 'Dolno Tserovene',
#           'short_name': 'Dolno Tserovene',
#           'types': ['locality', 'political']
#         },
#         {
#            'long_name': 'Montana Province',
#             'short_name': 'Montana Province',
#             'types': ['administrative_area_level_1', 'political']
#        },
#        {
#           'long_name': 'Bulgaria',
#           'short_name': 'BG',
#           'types': ['country', 'political']
#        },
#        {
#           'long_name': '3639',
#           'short_name': '3639',
#           'types': ['postal_code']
#         }],
#    'formatted_address': '3639 Dolno Tserovene, Bulgaria',
#    'geometry': {
#                   'bounds': {
#                       'northeast': {'lat': 43.5990104, 'lng': 23.2538839},
#                       'southwest': {'lat': 43.5792603, 'lng': 23.2217059}},
#                   'location': {'lat': 43.59026, 'lng': 23.2453677},
#                   'location_type': 'APPROXIMATE',
#                   'viewport': {
#                        'northeast': {'lat': 43.5990104, 'lng': 23.2538839},
#                        'southwest': {'lat': 43.5792603, 'lng': 23.2217059}
#                        }
#                 },
#     'place_id': 'ChIJKdUUh3qxVEcRECoOzRSgAAo',
#     'types': ['locality', 'political']}],
#     'status': 'OK'
# }