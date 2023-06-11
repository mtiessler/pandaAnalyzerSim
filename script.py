import pandas as pd
import matplotlib.pyplot as plt

FILE_PATH = 'ex6.csv'
COUNT_ROW = 22
DEFECTOR_INIT_COLUMN = 1
COOPERATOR_INIT_COLUMN = 2
DEFECTOR_COLOR = 'red'
COOPERATOR_COLOR = 'blue'


def plotTimeSeries(data, columns, init_column, title, ylabel, color):
    timeseries = range(len(columns[init_column::2]))
    timeseries_values = []
    for i in range(init_column, len(columns), 2):
        column = str(columns[i])
        timeseries_values.append(pd.to_numeric(data.loc[COUNT_ROW, column]))

    plt.plot(timeseries, timeseries_values, marker='o', linestyle='-', color=color)
    plt.xlabel('Time series')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()


def processTimeSeries(data):
    columns = data.columns

    plotTimeSeries(data,
                   columns,
                   COOPERATOR_INIT_COLUMN,
                   'Number of Cooperators over Time Series',
                   'Number of Cooperators',
                   COOPERATOR_COLOR)

    plotTimeSeries(data,
                   columns,
                   DEFECTOR_INIT_COLUMN,
                   'Number of Defectors over Time Series',
                   'Number of Defectors',
                   DEFECTOR_COLOR)


def readFile():
    try:
        data = pd.read_csv(FILE_PATH)
        processTimeSeries(data)
    except FileNotFoundError:
        print(f"File '{FILE_PATH}' not found.")
    except IOError:
        print(f"Error while processing: '{FILE_PATH}'.")


if __name__ == '__main__':
    readFile()
