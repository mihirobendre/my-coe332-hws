import math

def calculate_great_circle_distance(latitude1: float, longitude1: float, latitude2: float, longitude2: float) -> float:
    """
    Calculates the great-circle distance between two geographical coordinates.

    Args:
        latitude1: Latitude of the first location.
        longitude1: Longitude of the first location.
        latitude2: Latitude of the second location.
        longitude2: Longitude of the second location.

    Returns:
        Great-circle distance between the two locations in kilometers.
    """
    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(latitude1)
    lon1_rad = math.radians(longitude1)
    lat2_rad = math.radians(latitude2)
    lon2_rad = math.radians(longitude2)

    # Haversine formula
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = 6371 * c  # Earth's radius in kilometers
    return distance




