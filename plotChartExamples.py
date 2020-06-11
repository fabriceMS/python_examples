from matplotlib import pyplot as plt
from collections import Counter
import numpy as np
import pandas as pd
import csv


# Display graph line
def showLine():

    # Change the style
    #print(plt.style.available)
    plt.style.use('fivethirtyeight')

    # Get values and plot
    x_values = [24,25,26,27,28]
    y1_data = [40, 32, 100, 98, 55]
    plt.plot(x_values,y1_data, color='#5a7d9a', linestyle='--', marker='.', label='Female')

    x2_values = [24,25,26,27,28]
    y2_data = [140, 132, 100, 198, 155]
    plt.plot(x2_values,y2_data, color='#adad3b', linestyle='-', linewidth=2, marker='o', label='Male')
    #plt.bar(x2_values,y2_data, color='#adad3b')


    # Set chart title and label axes and legend
    plt.title('Median Salary by Ages')
    plt.ylabel('Median Salary')
    plt.xlabel('Ages')
    plt.legend()

    # Add a grid
    plt.grid(True)



    # Adjust and show plot
    plt.tight_layout()
    plt.show()

    # Save to a file
    plt.savefig('plot.png')


# Display graph bar
def showBar():
    ages_x = [24,25,26,27,28]
    x_indexes = np.arange(len(ages_x))
    width = 0.25

    y1_data = [40, 32, 100, 98, 55]
    plt.bar(x_indexes,y1_data, width=width, label='Female')

    y2_data = [140, 132, 100, 198, 155]
    plt.bar(x_indexes - width, y2_data, width=width, label='Male')

    # Adjust and show bar
    plt.legend()

    plt.xticks(ticks=x_indexes, labels=ages_x)


    plt.title('Bar Chart Test')
    plt.tight_layout()
    plt.show()



def showByCSV():
    plt.style.use('fivethirtyeight')

    with open('data.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        language_counter= Counter()

        for row in csv_reader:
            language_counter.update(row['LanguagesWorkedWith'].split(';'))
        # row = next(csv_reader)
        # print (row['LanguagesWorkedWith'].split(';'))

    # Print top 10
    print (language_counter.most_common(10))

    languages = []
    popularity = []

    # Get the X and Y axis
    for item in language_counter.most_common(10):
        languages.append(item[0])
        popularity.append(item[1])
    
    # print(languages)
    # print(popularity)

    # plot Horizontal bar chart 
    languages.reverse()
    popularity.reverse()
    plt.barh(languages, popularity)

    # Set chart title and label axes and legend
    plt.title('Top 10 popular languages')
    plt.xlabel('Number of people who use')
    plt.ylabel('Programming languages')
    plt.legend()
    plt.show()



def usePandaAndCSV():

    data = pd.read_csv('data.csv')
    
    # Put columns values into list
    ids = data['Responder_id']
    lang_responses = data['LanguagesWorkedWith']

    # Intialise the Counter (that count the number of occurence within a list)
    language_counter= Counter()

    for response in lang_responses:
        language_counter.update(response.split(';'))

    languages = []
    popularity = []

    # Get the X and Y axis
    for item in language_counter.most_common(10):
        languages.append(item[0])
        popularity.append(item[1])
    
    # print(languages)
    # print(popularity)

    # plot Horizontal bar chart 
    languages.reverse()
    popularity.reverse()
    
     # Set chart title and label axes and legend
    plt.title('Top 10 popular languages')
    plt.xlabel('Number of people who use')
    
    
    plt.tight_layout()
    plt.barh(languages, popularity)
    plt.show()



def pieChart():
    slices = [2, 5, 7]
    labels = [slices[0], slices[1], slices[2]]
    colors = ['blue', 'red', 'green']
    # Put the second value out of the pie chart out
    explode = [0, 0.1, 0]


    plt.pie(slices, labels=labels, explode=explode, colors=colors, wedgeprops={'edgecolor': 'black'}, shadow=True, autopct='%1.1f%%')
    plt.title("Pie Chart")
    plt.tight_layout()
    plt.show()



def betterPieChart():
    # Pie chart
    labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
    sizes = [15, 30, 45, 10]
    
    # only "explode" the 2nd slice (i.e. 'Hogs')
    explode = (0, 0.1, 0, 0)
    
    #add colors
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=90)
    # Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')
    plt.tight_layout()
    plt.show()



def betterBarChart():
    # set font
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'Helvetica'

    # set the style of the axes and the text color
    plt.rcParams['axes.edgecolor']='#333F4B'
    plt.rcParams['axes.linewidth']=0.8
    plt.rcParams['xtick.color']='#333F4B'
    plt.rcParams['ytick.color']='#333F4B'
    plt.rcParams['text.color']='#333F4B'

    # create some fake data
    percentages = pd.Series([20, 15, 18, 8, 6, 7, 10, 2, 10, 4], 
                            index=['Rent', 'Transportation', 'Bills', 'Food', 
                                'Travel', 'Entertainment', 'Health', 'Other', 'Clothes', 'Phone'])
    df = pd.DataFrame({'percentage' : percentages})
    df = df.sort_values(by='percentage')

    # we first need a numeric placeholder for the y axis
    my_range=list(range(1,len(df.index)+1))

    fig, ax = plt.subplots(figsize=(5,3.5))

    # create for each expense type an horizontal line that starts at x = 0 with the length 
    # represented by the specific expense percentage value.
    plt.hlines(y=my_range, xmin=0, xmax=df['percentage'], color='#007ACC', alpha=0.2, linewidth=5)

    # create for each expense type a dot at the level of the expense percentage value
    plt.plot(df['percentage'], my_range, "o", markersize=5, color='#007ACC', alpha=0.6)

    # set labels
    ax.set_xlabel('Percentage', fontsize=15, fontweight='black', color = '#333F4B')
    ax.set_ylabel('')

    # set axis
    ax.tick_params(axis='both', which='major', labelsize=12)
    plt.yticks(my_range, df.index)

    # add an horizonal label for the y axis 
    fig.text(-0.23, 0.96, 'Transaction Type', fontsize=15, fontweight='black', color = '#333F4B')

    # change the style of the axis spines
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_smart_bounds(True)
    ax.spines['bottom'].set_smart_bounds(True)

    # set the spines position
    ax.spines['bottom'].set_position(('axes', -0.04))
    ax.spines['left'].set_position(('axes', 0.015))

    #plt.savefig('hist2.png', dpi=300, bbox_inches='tight')
    plt.show()



def stackPlot():
    
    plt.style.use('fivethirtyeight')

    years = [2017, 2018, 2019, 2020]
    server1 = [2, 2, 4, 5]
    server2 = [2, 3, 4, 6]
    server3 = [2, 4, 2, 10]

    labels = ['server1', 'server2', 'server3']
    colors = ['#edf492','#efb960','#ee91bc']


    plt.stackplot(years, server1, server2, server3, labels=labels, colors=colors)
    
    plt.legend(loc='upper left')

    plt.title("Stack Plot Example")
    plt.tight_layout()
    plt.show()






def howCounterWorks():
    c = Counter(['Python', 'Java'])
    print (c)

    c.update(['Python', 'C++'])
    print (c)

    c.update(['Python', 'C++', 'Java'])
    print (c)

#####################
#       MAIN        #
#####################


if __name__ == "__main__":
    stackPlot()


