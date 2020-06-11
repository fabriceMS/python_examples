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
    usePandaAndCSV()


