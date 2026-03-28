import requests
API_KEY = "HXPV2NBRKN9JZJCK"
# Create stock_symbol function that asks which company's stock the user wishes to see
# Compare their choice with what is in the database and make sure it exists
# Return the symbol as a string

def stock_symbol():
    while True:
    # Ask the user which companys stock they want to see
        company = input("Which company's stock do you want to see? ")
        url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={company}&apikey={API_KEY}"
        r = requests.get(url)
        data = r.json()
        if "bestMatches" in data and data["bestMatches"]:
            symbol = data["bestMatches"][0]["1. symbol"]
            return symbol
        else:
            print("No matches found. Please check spelling and try again.")
    # Compare their choice with what is in the database and make sure it exists
    # If it does exist return the symbol as a string
    # If it does not exist ask the user to check their spelling/capitalization and try again




# Create the chart function that asks the user which chart they want to use (1 or 2)
def chart():
    while True:
        print("\n------- Chart Options -------")
        print("1. Line Chart")
        print("2. Bar Chart")
        chart_choice = input("Which chart do you want to use? (1 or 2): ")
        if chart_choice in ["1", "2"]:
            return chart_choice
        else:
            print("Invalid choice. Please enter 1 or 2.")
# Return their choice 



# Create the time_series function that asks the user which of the 4 time series options they want to have (1,2,3,4)
# return their choice



# Create the date_choice function that prompts the user to enter both the start and end date of the data 
# make sure that it is in yyyy-mm-dd format
# make sure that the end date is not before the start date



# Create the generate_graph function that takes all the information the user has selected and creates a graph
# That displays on the users default browser 


def main():
    while(True):
        # Call the function stock_symbol and store the data in symbol value
        symbol = stock_symbol()
        # Call the function chart and store the data in chart value
        chart_choice = chart()
        # Call the function time_series  and store the data in a time_series value

        # Call the function date_choice and store the dates in two different values: start_date, end_date

        # Call the function generate_graph

        # Ask the user if they wish to continue
        user_choice = input("Do you wish to continue (y/n): ")
        # If they press y or Y then loop back through the program
        if user_choice.lower() == "y":
            continue
        # else end the program
        else:
            break


# Call the main function
if __name__ == "__main__":
    main()