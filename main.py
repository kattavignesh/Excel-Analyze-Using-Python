import pandas as pd
import webbrowser

# Load the Excel file
file_path = 'stocks.xlsx'
stocks_df = pd.read_excel(file_path)

# Function to display stock data
def display_stock_data():
    print(stocks_df)

# Function to find the stock with the highest price
def get_high_price_stock():
    high_price_stock = stocks_df.loc[stocks_df['Stock Price'].idxmax()]
    return high_price_stock

# Function to find the stock with the lowest price
def get_low_price_stock():
    low_price_stock = stocks_df.loc[stocks_df['Stock Price'].idxmin()]
    return low_price_stock

# Main function to interact with the user
def main():
    while True:
        user_input = input("\nTHIS PROJECT IS REGARDING THE BEST STOCKS IN 2024 THAT PERFORMED WELL.\n\n Enter 'DISPLAY' to show stock data\n Enter 'HIGH' for the highest price stock\n Enter 'LOW' for the lowest price stock\n Enter 'ANALYSE' to run analysis\n Enter 'EXIT' to quit\n\n Please enter your input: ").strip().lower()
        
        if user_input == 'display':
            display_stock_data()
        elif user_input == 'high':
            print("Stock with the highest price:")
            print(get_high_price_stock())
        elif user_input == 'low':
            print("Stock with the lowest price:")
            print(get_low_price_stock())
        elif user_input == 'analyse':
            print("Running analysis...")
            with open('analysis.py') as f:
                exec(f.read())
        elif user_input == 'exit':
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()

user=input("\nNeed More Stocks? Enter 'YES' or 'NO':")
if user=='yes':
    print("Please Wait...")
    webbrowser.open("https://www.marketwatch.com/")
elif user == 'no':
    print("No problem. Have a nice day!")
else:
    print("Invalid input. Exiting...")
    print("Exited Successfully, Thankyou.")
    exit()

