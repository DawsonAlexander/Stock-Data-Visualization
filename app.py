import requests
from datetime import datetime
import pygal
import lxml
import csv
from flask import Flask, render_template, request, flash, redirect, url_for
API_KEY = "HXPV2NBRKN9JZJCK"
# Create stock_symbol function that asks which company's stock the user wishes to see
# Compare their choice with what is in the database and make sure it exists
# Return the symbol as a string
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/', methods=['GET'])
def index():
    #read all of the stock symbols from the csv file
    with open('stocks.csv', mode='r', newline='') as file:
        reader =csv.DictReader(file)
        stocks = list(reader)
    return render_template('index.html', stock_symbol=stocks)

@app.route('/', methods=['POST'])
def index_post():
    #get the current date
    now = datetime.now()
    #get the stock symbol, the chart type, the function, the start and end date
    symbol = request.form.get('Stock_Symbol')
    chart = request.form.get('Chart_Type')
    function=request.form.get('function')
    start_date_str = request.form.get('start_date')
    end_date_str = request.form.get('end_date')
    
    #check if each one is empty and flash an error if it is
    if not symbol:
        flash('Symbol is required.', 'error')
        return redirect(url_for('index'))
    if not chart:
        flash('Chart is required.', 'error')
        return redirect(url_for('index'))
    if not function:
        flash('Function is required.', 'error')
        return redirect(url_for('index'))
    if not start_date_str:
        flash('Start Date is required.', 'error')
        return redirect(url_for('index'))
    if not end_date_str:
        flash('End Date is required.', 'error')
        return redirect(url_for('index'))

    #convert the start and end date into yyyy-mm-dd format
    try:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    #throw an error if it isn't able to conver
    except ValueError:
        flash('Invalid date format.', 'error')
        return redirect(url_for('index'))    

    #Check if start date is after end date
    if start_date > end_date:
        flash('Start date cannot be after end date.' , 'error')
        return redirect(url_for('index'))
    #Make sure that the start date and end date aren't after the current date
    if start_date > now or end_date > now:
        flash('Start date or End Date cannot be after the current date', 'error')
        return redirect(url_for('index'))
    
    #get the data with the app_data function
    data = app_data(function, symbol, start_date, end_date, API_KEY)
    #generate the graph 
    graph = generate_graph(chart, data, function, symbol)
    #read all of the stock symbols from the csv file
    with open('stocks.csv', mode='r', newline='') as file:
        reader =csv.DictReader(file)
        stocks = list(reader)
    
    #render the index.html template and populate the stock symbol for loop and display the graph
    return render_template('index.html',stock_symbol=stocks, graph=graph)
    


# def stock_symbol():
#     while True:
#         #API_KEY = "demo"
#     # Ask the user which companys stock they want to see
#         company = input("Which company's stock do you want to see?(If you want intraday data use IBM It is the only one avaliable.) ")
#         url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={company}&apikey={API_KEY}"
#         r = requests.get(url)
#         data = r.json()
#         if "bestMatches" in data and data["bestMatches"]:
#             symbol = data["bestMatches"][0]["1. symbol"]
#             return symbol
#         else:
#             print("No matches found. Please check spelling and try again.")
#             continue
#     # Compare their choice with what is in the database and make sure it exists
#     # If it does exist return the symbol as a string
#     # If it does not exist ask the user to check their spelling/capitalization and try again




# # Create the chart function that asks the user which chart they want to use (1 or 2)
# def chart():
#     while True:
#         print("\n------- Chart Options -------")
#         print("1. Line Chart")
#         print("2. Bar Chart")
#         chart_choice = input("Which chart do you want to use? (1 or 2): ")
#         if chart_choice in ["1", "2"]:
#             return chart_choice
#         else:
#             print("Invalid choice. Please enter 1 or 2.")
# # Return their choice 


# # Create the time_series function that asks the user which of the 4 time series options they want to have (1,2,3,4)
# # return their choice
# def time_series():
#     # ask the user for either 1,2,3,4
#     # if not prompt them again
#     while(True):
#         print("-----------------\nChoose an option:\n1)Intra Day\n2)Daily\n3)Weekly\n4)Monthly")
#         time_series_choice = input("Please make a selection: ")
#         if time_series_choice == "1":
#             return "TIME_SERIES_INTRADAY"
#         elif time_series_choice == "2":
#             return "TIME_SERIES_DAILY"
#         elif time_series_choice =="3":
#             return "TIME_SERIES_WEEKLY"
#         elif time_series_choice == "4":
#             return "TIME_SERIES_MONTHLY"
#         else:
#             print("Please choose either 1, 2, 3, or 4")
#             continue
            


# # Create the date_choice function that prompts the user to enter both the start and end date of the data 
# # make sure that it is in yyyy-mm-dd format
# # make sure that the end date is not before the start date
# def date_choice(function, symbol, api_key):
#     while True:
#         # get and validate start date
#         while True:
#             start_input = input("Enter the start date (YYYY-MM-DD): ").strip()
#             try:
#                 start_date = datetime.strptime(start_input, "%Y-%m-%d")
#                 break
#             except ValueError:
#                 print("Invalid format. Please enter the date as YYYY-MM-DD.")

#         # get and validate end date
#         while True:
#             end_input = input("Enter the end date (YYYY-MM-DD): ").strip()
#             try:
#                 end_date = datetime.strptime(end_input, "%Y-%m-%d")
#                 break
#             except ValueError:
#                 print("Invalid format. Please enter the date as YYYY-MM-DD.")

#         # make sure end date is not before start date
#         if end_date < start_date:
#             print("Error: End date cannot be before the start date. Please try again.")
#             continue

#         # call the existing app_data function
#         data = app_data(function, symbol, start_input, end_input, api_key)

#         # if app_data returns empty, prompt user to pick new dates
#         if not data:
#             print("No data found for that date range. Please choose a different range.")
#             continue

#         return data

        

    


# Create a app_data function that gets the stock data from alpha vantage using the symbol and function the user selected 
# and return it to the main function
def app_data(function, symbol, start_date, end_date, api_key):
    # If the function selected is Intraday then have the url have an interval of 5mins

    #for testing use this 
    #Intraday is  a premimum end point meaning you must use 'demo' key to get results
    #api_key="demo"
    if function == "TIME_SERIES_INTRADAY":
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_{function}&symbol={symbol}&interval=5min&apikey=demo'
        r = requests.get(url)
        data = r.json()
        #print(data)
        #Extract the correct time series key
        time_series = data.get("Time Series (5min)", {})
        
        # For error checking
        #print(time_series)
        return time_series
    
    else:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_{function}&symbol={symbol}&apikey={api_key}'
        r = requests.get(url)
        data = r.json()
        #print(data)
        # Get common keys for daily, weekly, and monthly
        time_series = (
            data.get("Time Series (Daily)") or
            data.get("Weekly Time Series") or 
            data.get("Monthly Time Series") or {}
        )

        # Make sure it is in yyyy-mm-dd format
        range_start = start_date
        range_end = end_date

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
            #print(sorted(time_series.keys()))

        # For error checking
        #print(filtered_data)
        return filtered_data


# Create the generate_graph function that takes all the information the user has selected and creates a graph
# That displays on the users default browser 

def generate_graph(chart, data, time_series_choice, symbol):
    #Sort the data keys which is the dates and then store them in a list called dates
    sorted_dates = sorted(data.keys())
    # Create empty lists for dates, open, close, high, low
    dates = []
    open_prices = []
    close_prices = []
    high_prices = []
    low_prices = []
    

    #Loop through each date in sorted date and add the values to each list

    for date in sorted_dates:
        values = data[date]
        dates.append(date[:10])
        open_prices.append(float(values["1. open"]))
        high_prices.append(float(values["2. high"]))
        low_prices.append(float(values["3. low"]))
        close_prices.append(float(values["4. close"]))
        
    #If chart is equal to "1" create a line chart
    if chart == "Line":
        line_chart = pygal.Line()
        line_chart.title =f'{time_series_choice} for {symbol}'
        line_chart.x_labels = dates
        line_chart.add("Open", open_prices)
        line_chart.add("High", high_prices)
        line_chart.add("Low", low_prices)
        line_chart.add("Close", close_prices)
        

        return line_chart.render_data_uri()
    #if the chart is equal to "2" then create a bar chart
    elif chart == "Bar":
        bar_chart = pygal.Bar()
        bar_chart.title =f'{time_series_choice} for {symbol}'
        bar_chart.x_labels = dates
        bar_chart.add("Open", open_prices)
        bar_chart.add("High", high_prices)
        bar_chart.add("Low", low_prices)
        bar_chart.add("Close", close_prices)

        return bar_chart.render_data_uri()
        
    
    return



# def main():
#     while(True):
#         # Call the function stock_symbol and store the data in symbol value
#         symbol = stock_symbol()
        
#         # Call the function chart and store the data in chart value
#         chart_choice = chart()
        
#         # Call the function time_series  and store the data in a time_series value
#         time_series_choice = time_series()

#         # Call the function date_choice and store the dates in two different values: start_date, end_date
#         data = date_choice(time_series_choice, symbol, API_KEY)
#         # Call the function generate_graph
#         generate_graph(chart_choice, data, time_series_choice, symbol)
#         # Ask the user if they wish to continue
#         user_choice = input("Do you wish to continue (y/n): ")
#         # If they press y or Y then loop back through the program
#         if user_choice.lower() == "y":
#             continue
#         # else end the program
#         else:
#             print("Ending Program...")
#             break


# Call the main function
if __name__ == "__main__":
    app.run(debug=True, port=5019)