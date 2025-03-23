### MY 3 ---Part 3 (Test code.003)


# Import date and time
import datetime

def get_current_datetime():  # Get current date and time
    # Return the date and time
    return datetime.datetime.now()

# Save invoice
def save_invoice_to_file(invoice):
    # Save the invoice details to a text file
    file_name = f"invoice_{get_current_datetime().strftime('%Y%m%d_%H%M%S')}.txt"

    # Open the file in write mode and save the invoice details
    with open(file_name, 'w') as file:
        file.write("Invoice Details:\n")  # Write invoice details in the text file
        file.write(f"Date: {invoice['Start_city']}\n")  # Assuming 'Start_city' contains the start city name
        file.write(f"Customer: {invoice['End_city']}\n")  # Assuming 'End_city' contains the end city name
        file.write(f"Total Amount: {invoice['amount']}\n")  # Assuming 'amount' contains the total travel amount
        file.write(f"Promo Amount: {invoice['promo_code']}\n")  # Assuming 'promo_amount' contains the discounted amount using the promo code
        file.write(f"Random Reduction: {invoice['random_reduction']}\n")  # Assuming 'random_reduction' contains the reduction amount for lucky passengers
        file.write(f"Final Payment: {invoice['final_payment']}\n")  # Assuming 'final_payment' contains the final payment after discounts and reductions
        # Add more invoice details as needed

    print(f"Invoice successfully saved to {file_name}")  # Print the message invoice was saved