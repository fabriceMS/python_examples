import pandas as pd
import random
from itertools import count
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
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



# Read CSV File and define plot
def animate(i):
    data = pd.read_csv('live.csv')
    x_values = data['Responder_id']
    y_values = data['Age']

    # Clear Axis
    plt.cla()
    plt.plot(x_values, y_values)
    plt.tight_layout()

def plot_live_data():
    plt.style.use('seaborn-dark-palette')


    # Run the animate function every 1000ms (every seconds) --> This will plot updated values
    ani = FuncAnimation(plt.gcf(), animate, interval=1000)

    # Automatic pading
    plt.tight_layout()

    # Show plot
    plt.show()

if __name__ == "__main__":
    #print(plt.style.available)
    plot_live_data()