from DataObjects.utilities import load_object
from GeoUtilities.google_address import GoogleGeocodingData
import os


if __name__ == '__main__':

    path = os.path.abspath(__file__ + "/../../")
    filepath = path + r'\Data\dict.risk.addresses'

    c_raw = load_object(filepath)
    c_google = [GoogleGeocodingData(el) for el in c_raw.values()]
    c_addresses = [el.default_address for el in c_google]
    c_filter = [item for item in c_raw.items() if 'АРАБАКОНАК' in item[0]]

    a = 5