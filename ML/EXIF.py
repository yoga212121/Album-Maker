from exif import Image
from geopy.geocoders import Nominatim

#image path must be in same folder
img_path = "Album-Maker/ML/food.jpg"    

def decimal_coords(coords, ref):
    decimal_degrees = coords[0]+coords[1]/60+coords[2]/3600
    if ref == "S" or ref == "W":
        decimal_degrees *= -1
    return decimal_degrees

def image_coordinates(img_path):
    with open(img_path, "rb") as src:
        img = Image(src)

    if img.has_exif:
        try:
            coords = (decimal_coords(img.gps_latitude, img.gps_latitude_ref), decimal_coords(img.gps_longitude, img.gps_longitude_ref))
            print(f"Image {src.name}, OS Version: {img.get('software', 'Not Known')} ---------")
            print(f"Was taken: {img.datetime_original}, has coordinates: {coords}")

            # Reverse geocode the coordinates using OpenStreetMap Nominatim API
            geolocator = Nominatim(user_agent="my-app")
            location = geolocator.reverse(coords)
            print(f"Location: {location.address}")

        except AttributeError:
            print("No Coordinates")
    else:
        print("The Image has no EXIF Info")

image_coordinates(img_path)

