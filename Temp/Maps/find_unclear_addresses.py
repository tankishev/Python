from DataObjects.utilities import load_object
from GeoUtilities.google_address import GoogleGeocodingData, GoogleAddress
from GeoUtilities.utilities import google_address_filter
from itertools import compress


c_path = r'Data\dict.clients.addresses'
r_path = r'Data\dict.risk.addresses'
c_raw = load_object(c_path)
r_raw = load_object(r_path)
c_data = [GoogleGeocodingData(el) for el in c_raw.values()]
r_data = [GoogleGeocodingData(el) for el in r_raw.values()]
c_data = list(filter(lambda item: item.status == 'OK', c_data))
r_data = list(filter(lambda item: item.status == 'OK', r_data))

r_adr = [GoogleAddress(adr) for el in r_data for adr in el.results]
c_adr = [GoogleAddress(el.default_address) for el in r_data]
output = []
for i, adr in enumerate(r_adr):
    if len(adr) < 4:
        output.append(adr)

print(*output, sep='\n')
