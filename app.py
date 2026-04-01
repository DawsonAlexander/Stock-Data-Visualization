import requests
from datetime import datetime
api_key="HXPV2NBRKN9JZJCK"

# Create stock_symbol function that asks which company's stock the user wishes to see
# Compare their choice with what is in the database and make sure it exists
# Return the symbol as a string


# Create the chart function that asks the user which chart they want to use (1 or 2)
# Return their choice 


# Create the time_series function that asks the user which of the 4 time series options they want to have (1,2,3,4)
# return their choice
def time_series():
    # ask the user for either 1,2,3,4
    # if not prompt them again
    while(True):
        print("-----------------\nChoose an option:\n1)Intra Day\n2)Daily\n3)Weekly\n4)Monthly")
        time_series_choice = input("Please make a selection: ")
        if time_series_choice == "1":
            return "TIME_SERIES_INTRADAY"
        elif time_series_choice == "2":
            return "TIME_SERIES_DAILY"
        elif time_series_choice =="3":
            return "TIME_SERIES_WEEKLY"
        elif time_series_choice == "4":
            return "TIME_SERIES_MONTHLY"
        else:
            print("Please choose either 1, 2, 3, or 4")
            continue
            


# Create the date_choice function that prompts the user to enter both the start and end date of the data 
# make sure that it is in yyyy-mm-dd format
# make sure that the end date is not before the start date
# In the date_choice function run the app_data function and if the app_data returns empty prompt the user to input new dates

        

    


# Create a app_data function that gets the stock data from alpha vantage using the symbol and function the user selected 
# and return it to the main function
def app_data(function, symbol, start_date, end_date, api_key):
    # If the function selected is Intraday then have the url have an interval of 5mins

    #for testing use this 
    api_key="demo"
    if function == "TIME_SERIES_INTRADAY":
        url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval=5min&apikey={api_key}'
        r = requests.get(url)
        data = r.json()
        
        #Extract the correct time series key
        time_series = data.get("Time Series (5min)", {})

        # For error checking
        print(time_series)
        return time_series
    
    else:
        url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={api_key}'
        r = requests.get(url)
        data = r.json()

        # Get common keys for daily, weekly, and monthly
        time_series = (
            data.get("Time Series (Daily)") or
            data.get("Weekly Time Series") or 
            data.get("Monthly Time Series") or {}
        )

        # Make sure it is in yyyy-mm-dd format
        range_start = datetime.strptime(start_date, '%Y-%m-%d')
        range_end = datetime.strptime(end_date, '%Y-%m-%d')

        # Filter the data within the start and end date
        filtered_data = {}
        for date_str, values in time_series.items():
            date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S' if " " in date_str else '%Y-%m-%d' )
            if range_start <= date_obj <= range_end:
                filtered_data[date_str] = values

        # If filtered_data is empty then give range of available dates
        if not filtered_data:
            print("No data for the selected date range.")
            #This lists all the possible dates they can choose (its a lot of dates)
            #only use for testing
            print(sorted(time_series.keys()))

        # For error checking
        print(filtered_data)
        return filtered_data


# Create the generate_graph function that takes all the information the user has selected and creates a graph
# That displays on the users default browser 


def main():
    while(True):
        # Call the function stock_symbol and store the data in symbol value
        #symbol=stock_symbol()

        # For testing
        symbol="IBM"
        # Call the function chart and store the data in chart value

        # Call the function time_series  and store the data in a time_series value
        time_series_choice = time_series()

        # Call the function date_choice and store the filtered data in a data value and send it to the generate_graph 
        # data = date_choice(time_series_choice, symbol, api_key)

        #For testing
        start_date = "2026-02-06"
        end_date = "2026-03-02"
        data = app_data(time_series_choice, symbol, start_date, end_date, api_key)
        
        # Call the function generate_graph
        
        # Ask the user if they wish to continue
        user_choice = input("Do you wish to continue (y/n): ")
        # If they press y or Y then loop back through the program
        if user_choice.lower() == "y":
            continue
        # else end the program
        else:
            print("Ending Program...")
            break


# Call the main function
if __name__ == "__main__":
    main()