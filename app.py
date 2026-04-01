# Create stock_symbol function that asks which company's stock the user wishes to see
# Compare their choice with what is in the database and make sure it exists
# Return the symbol as a string


# Create the chart function that asks the user which chart they want to use (1 or 2)
# Return their choice 



# Create the time_series function that asks the user which of the 4 time series options they want to have (1,2,3,4)
# return their choice



# Create the date_choice function that prompts the user to enter both the start and end date of the data 
# make sure that it is in yyyy-mm-dd format
# make sure that the end date is not before the start date
def date_choice(function, symbol, api_key):
    while True:
        # get and validate start date
        while True:
            start_input = input("Enter the start date (YYYY-MM-DD): ").strip()
            try:
                start_date = datetime.strptime(start_input, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid format. Please enter the date as YYYY-MM-DD.")

        # get and validate end date
        while True:
            end_input = input("Enter the end date (YYYY-MM-DD): ").strip()
            try:
                end_date = datetime.strptime(end_input, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid format. Please enter the date as YYYY-MM-DD.")

        # make sure end date is not before start date
        if end_date < start_date:
            print("Error: End date cannot be before the start date. Please try again.")
            continue

        # call the existing app_data function
        data = app_data(function, symbol, start_input, end_input, api_key)

        # if app_data returns empty, prompt user to pick new dates
        if not data:
            print("No data found for that date range. Please choose a different range.")
            continue

        return start_input, end_input, data



# Create the generate_graph function that takes all the information the user has selected and creates a graph
# That displays on the users default browser 


def main():
    while(True):
        # Call the function stock_symbol and store the data in symbol value

        # Call the function chart and store the data in chart value

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