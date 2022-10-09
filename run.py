import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

# Collect sales data from the user
# Add sales data into sales worksheet
# Calculate surplus number
# Add surplus data to surplus worksheet
# Calculate the average sales for the last 5 markets
# Add Calculated stock numbers into the stock worksheet
# Print stick recommendations to the terminal
# Check that the sales data input from the user is valid

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Love_sandwiches')


def get_sales_data():
    """
    Get Sales figures input from the user.
    Run a while loop to collect a vlid string of data from the user
    via the terminal, which must be a string of 6 number separated
    by commas. The loop will repeatedly request datam until it is valid. 
    """
    while True:    
        print("Enter Sales data from the last Market.")
        print("Data should be siz numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")

        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid")
            break 
    
    return sales_data


def validate_data(values):
    """
     Inside the try, converts all string values into integers.
     Raises valueError if Strings cannot be converted into int,
     or if there aren't exactly 6 values.

    """
    try: 
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n")
        return False

    return True


def update_sales(data):
    """
    Update sales worksheet, add new row with the list data provided
    """
    print("Updating sales worksheet..... \n")

    sales_worksheet = SHEET.worksheet('sales')
    sales_worksheet.append_row(data)
    print('Sales worksheet updated succesfully.\n')


def calculate_surplus_data(sales_row):
    """
    Compare sales with stick and calculate the surplus for each item type.

    The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made when stock was sold out
    """

    print("Caculating surplus data...\n")
    stock = SHEET.worksheet('stock').get_all_values()
    stock_row = stock[-1]
    print("Stock row ", stock_row)
    print("sales row: ", sales_row)

    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
   
    return surplus_data


def main():
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    # update_sales(sales_data)
    new_surplus = calculate_surplus_data(sales_data)
    print('surplus : ', new_surplus)


print('\nWelcome to Love Sandwiches Data Automation\n')
main()