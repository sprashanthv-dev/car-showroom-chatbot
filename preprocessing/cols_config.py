excluded_cols = ["salvage", "savings_amount", "theft_title",
                 "trimId", "vehicle_damage_category", "cabin", "isCab", "is_certified",
                 "is_cpo", "is_oemcpo", "dealer_zip", "bed", "bed_height", "bed_length",
                 "combine_fuel_economy", "fleet", "frame_damaged"]

numeric_columns = ['back_legroom', 'front_legroom', 'fuel_tank_volume', 'height', 'length', 'wheelbase', 'width']

description_regex = "[!@@Additional Info@@!]"

transmission_types = {
    "A": "Automatic",
    "M": "Manual",
    "CVT": "Continuously Variable Transmission",
}

MAX_COMPETITORS = 5
