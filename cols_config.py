excluded_cols = ["main_picture_url", "salvage", "savings_amount", "theft_title",
                 "trimId", "vehicle_damage_category", "cabin", "isCab", "is_certified",
                 "is_cpo", "is_oemcpo", "dealer_zip", "bed", "bed_height", "bed_length",
                 "combine_fuel_economy", "fleet", "frame_damaged"]

numeric_columns = ['city_fuel_economy', 'daysonmarket', 'engine_displacement',
                   'highway_fuel_economy', 'mileage', 'owner_count', 'price',
                   'seller_rating', 'listing_id', 'latitude', 'longitude']

description_regex = "[!@@Additional Info@@!]"

transmission_types = {
    "A": "Automatic",
    "M": "Manual",
    "CVT": "Continuously Variable Transmission",
}

MAX_COMPETITORS = 5

col_types = {
    'vin': str,
    'back_legroom': str,
    'body_type': str,
    'city': str,
    'city_fuel_economy': float,
    'daysonmarket': int,
    'description': str,
    'engine_cylinders': str,
    'engine_displacement': float,
    'engine_type': str,
    'exterior_color': str,
    'franchise_dealer': str,
    'franchise_make': str,
    'front_legroom': str,
    'fuel_tank_volume': str,
    'fuel_type': str,
    'has_accidents': str,
    'height': str,
    'highway_fuel_economy': float,
    'horsepower': str,
    'interior_color': str,
    'is_new': str,
    'latitude': float,
    'length': str,
    'listed_date': str,
    'listing_color': str,
    'listing_id': int,
    'longitude': float,
    'major_options': str,
    'make_name': str,
    'maximum_seating': str,
    'mileage': float,
    'model_name': str,
    'owner_count': float,
    'power': str,
    'price': float,
    'seller_rating': float,
    'sp_id': int,
    'sp_name': str,
    'torque': str,
    'transmission': str,
    'transmission_display': str,
    'trim_name': str,
    'wheel_system': str,
    'wheel_system_display': str,
    'wheelbase': str,
    'width': str,
    'year': int
}
