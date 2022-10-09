import gspread
from google.oauth2.service_account import Credentials

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
     get Sales figures input from the user
    """

    print("Enter Sales data from the last Market.")
    print("Data should be siz numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ")
    data_str = input(f"The data provided is {data_str}")


get_sales_data()