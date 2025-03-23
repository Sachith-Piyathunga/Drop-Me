from asyncio.windows_events import NULL
import sys
from Pakages.invoice import save_invoice_to_file, get_current_datetime
from Pakages.citypricerate import get_price_chart, apply_promo, get_random_reduction,get_promo_codes,get_travel_price

def print_prices(chart,vehicle,multiplier):
    print(f"--------{vehicle}--------")
    for city1,cities in chart.items():
        for city2,price in cities.items():
            print(f"{city1} to {city2}: {price*multiplier}")
    print()
    print()

def main(arg):
    
    #print("Arguments:", sys.argv)
    print("\n")


    if sys.argv[0] == 'dm.py':
        if sys.argv[1] == '/price':
            # The price command shows the full price plan for the whole City
            price_chart = get_price_chart()
            print_prices(price_chart,"Trishaw",1)
            print_prices(price_chart,"Car",2)
            print_prices(price_chart,"Van",3)



        elif sys.argv[1] == '/?':
            # Handle the /? command to show how the "dm" command functions
            print("Usage:")
            print("dm /price - Show the full price plan for the travel whole City")
            print("dm Start City End City [/c | /v] [PromoCode]")
            print("Calculate the Travel price from StartCity to End City with optional vehicle preference and promo code.")
        else:
            # If none of the above commands are used, it assumes the user wants to perform a travel calculation.
            start_city = sys.argv[1].capitalize()
            end_city = sys.argv[2].capitalize()
            multiplier = 1  # Set default vehicle to 'Trishaw' with a multiplier of 1
            promo_code = ""   # Set promo code as none because no promo codes applied by default


            if len(sys.argv) >= 5:
                # Check if a promo code is provided
                promo_code = sys.argv[4].lower()

            print(f"{start_city}, {end_city}, {promo_code}")


            if len(sys.argv) >= 4:
                # Check if a vehicle preference is provided (Car or Van)
                if sys.argv[3] == '/c':
                    multiplier = 2  # Car has multiplier 2
                elif sys.argv[3] == '/v':
                    multiplier = 3  # Van has multiplier 3


            price_chart = get_price_chart()  # Get the price chart
            travel_price = get_travel_price(price_chart, start_city, end_city, multiplier)
            print(f"{price_chart.keys()}")

            if promo_code and promo_code in get_promo_codes():  # Apply the promo code if it is valid
                discounted_amount = apply_promo(travel_price, promo_code)
                final_payment = max(0, discounted_amount)  # Final payment cannot be negative ( If the traveler traveled around the cities )
                random_reduction = 0
            else:
                random_reduction = get_random_reduction()  # If no valid promo code is provided, generate a random reduction value for lucky passengers
                final_payment = max(0, travel_price - random_reduction)  # Final payment must be positive

            current_datetime = get_current_datetime()   # Get the current date and time
            invoice = {
                'Start_city': start_city,
                'End_city': end_city,
                'amount': travel_price,
                'promo_code': promo_code,
                'random_reduction': random_reduction,
                'final_payment': final_payment
            }

            save_invoice_to_file(invoice)  # Save invoice details in a text file
            # Print invoice details to the console
            print(f"Date : {current_datetime.strftime('%Y-%m-%d')}")
            print(f"Time: {current_datetime.strftime('%H:%M:%S')}")
            print(f"Start : {start_city}")
            print(f"End : {end_city}")
            print(f"Amount : {travel_price} KMD")
            if promo_code:
                print(f"Promo : {promo_code}")
            print(f"Random Reduction : {random_reduction} KMD")
            print(f"Final payment : {final_payment} KMD")

if __name__ == "__main__":
    main(sys.argv[1:])


