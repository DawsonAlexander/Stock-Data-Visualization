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
        print("-----------------\nChoose an option:\n1)Intra day\n2)Daily\n3)Weekly\n4)Monthly")
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



# Create the generate_graph function that takes all the information the user has selected and creates a graph
# That displays on the users default browser 


def main():
    while(True):
        # Call the function stock_symbol and store the data in symbol value
        
        # Call the function chart and store the data in chart value

        # Call the function time_series  and store the data in a time_series value
        time_series_choice = time_series()

        # Call the function date_choice and store the dates in two different values: start_date, end_date

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