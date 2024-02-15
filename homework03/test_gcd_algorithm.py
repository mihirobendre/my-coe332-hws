from gcd_algorithm import calculate_great_circle_distance

def test_calculate_great_circle_distance():
    assert calculate_great_circle_distance(1,2,3,-4.0) == 702.8403217956061

#calculate_great_circle_distance(latitude1: float, longitude1: float, latitude2: float, longitude2: float)
