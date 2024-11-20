"""

Driver: Idil Ibrahim
Navigator: None
Assignment: Excersie 11
Date: 11/19/24
Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

# Imports 
import sys
import argparse
import requests

def get_holidays(country_code, year):

    """
    Retreives and display the holidays for a country and year. 

    Args: 
        Country_code (str): Two letter code for the country
        year (int): Four-digit year to egt holidays for.
    
    """
    # Create the URL using the country code and year 
    url = f"https://date.nager.at/api/v3/publicholidays/{year}/{country_code}"

    #Makes the requests to get holiday data fro API
    response = requests.get(url)

    #Checks the reponse
    if response.status_code == 200:
        holidays = response.json()

        #Loops through the holiday and prints the name and date 
        for holiday in holidays:
            print(f"{holiday['date']}: {holiday['localName']}")
        else: 
            #Prints an error message
            print("There was an error getting holiday data. Please check your input")

def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as arguments
    
    Args:
        args_list (list): List of command-line arguments.
    Returns:
        argparse.Namespace: Parsed arguments as an object.
    """

    # The parser handles command-line arguments
    parser = argparse.ArgumentParser(description="Retieve public holidays for a specific country and year.")
    parser.add_argument('country_code', type=str, help='Two-letter country code (ISO Alpha-2).')
    parser.add_argument('year', type=int, help='Four-digit year.')
    args = parser.parse_args(args_list)  # Parse the list of command-line arguments
    return args #reutrns 

def main(country_code, year):
    """
    Main function to print holidays based on the input 

    Args: 
     country_code (str): The country code provided as input.
        year (int): The year provided as input

    """
    get_holidays(country_code, year) # call the function to get the holiday display


if __name__ == "__main__":
    arguments = parse_args(sys.argv[1:]) #Pass in the list of command line arguments to the parse_args function.
    main (arguments.country_code, arguments.year)
