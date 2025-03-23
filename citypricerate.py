### MY 2 ---Part 2 (Test code.002)

# Import City names and all the travel prices
def create_city_constants():  # Constants show the city names
    return {
        'Alvin': 'Alvin',
        'James': 'James',
        'Razi': 'Razi',
        'Mali': 'Mali',
        'Zuhar': 'Zuhar',
    }

# Import City
def get_city_constants():
    return create_city_constants()

def create_price_chart():  # Create travel prices chart
    city_constants = create_city_constants()
    price_chart = {
        'Alvin': {  # Between Alvin to other cities
            'Alvin': 0,
            'James': 20,
            'Razi': 40,
            'Mali': 40,
            'Zuhar': 20,
        },
        'James': {  # Between James to other cities
            'Alvin': 20,
            'James': 0,
            'Razi': 20,
            'Mali': 40,
            'Zuhar': 40,
        },
        'Razi': {  # Between Razi to other cities
            'Alvin': 40,
            'James': 20,
            'Razi': 0,
            'Mali': 20,
            'Zuhar': 40,
        },
        'Mali': {  # Between Mali to other cities
            'Alvin': 40,
            'James': 40,
            'Razi': 20,
            'Mali': 0,
            'Zuhar': 20,
        },
        'Zuhar': {   # Between Zuhar to other cities
            'Alvin': 20,
            'James': 40,
            'Razi': 40,
            'Mali': 20,
            'Zuhar': 0,
        },
    }
    return price_chart

def get_price_chart():
    return create_price_chart()
    # Calculate the price based on start city and end city, and the vehicle type
def get_travel_price(price_chart, start_city, end_city, multiplier):

    if start_city not in price_chart.keys():
        raise ValueError("Invalid start or end city.")

    if multiplier <= 0:
        raise ValueError("Invalid vehicle multiplier.")

    price = price_chart[start_city][end_city] * multiplier
    return price


# Get the promo services
import random

def create_promo_codes():  # Create the list for available promo codes
    return ['pro2', 'pro5', 'pro10']

def get_promo_codes():
    return create_promo_codes()

def apply_promo(amount, promo_code):
    # Applying the promo code and return the discounted amount
    promo_codes = create_promo_codes()

    if promo_code not in promo_codes:
        raise ValueError("Invalid promo code.")

    if promo_code == 'pro2':
        return amount * 0.98  # Give 2% discount
    elif promo_code == 'pro5':
        return amount * 0.95  # Give 5% discount
    elif promo_code == 'pro10':
        return amount * 0.9  # Give 10% discount

def get_random_reduction():
    # Generate random reduction value for lucky passengers and return it
    return random.randint(0, 15)  # Randomly get lucky passengers
