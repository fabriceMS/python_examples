import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates


# Ex: Plot a graph with date in axis
def plot_time_serie():
    # Define the style
    plt.style.use('seaborn')

    # Read CSV file using Pandas
    data = pd.read_csv('data_TimeSeries.csv')

    # Convert the Date field into a python DateTime and sort it (instead of string)
    data['Date'] = pd.to_datetime(data['Date'])
    data.sort_values('Date', inplace=True)

    # Get values
    price_date = data['Date']
    price_close = data['Close']

    # Plot the graph using the plot_date function
    plt.plot_date(price_date, price_close, linestyle='solid')

    # Specify a format for the date
    date_format = mpl_dates.DateFormatter('%b, %d %Y')
    plt.gca().xaxis.set_major_formatter(date_format)

    # Auto format the date (to be more readable)
    #plt.gcf().autofmt_xdate()

    # Format the graph
    plt.title('Bitcoin Prices')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')

    plt.tight_layout()

    # Display the graph
    plt.show()


if __name__ == "__main__":
    plot_time_serie()