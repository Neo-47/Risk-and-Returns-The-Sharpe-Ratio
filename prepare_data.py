import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Reading in the data
stock_data = pd.read_csv("datasets/stock_data.csv", index_col = 'Date', parse_dates=True)
benchmark_data = pd.read_csv("datasets/benchmark_data.csv", index_col = 'Date', parse_dates=True)
benchmark_data = benchmark_data.dropna()



if __name__ == '__main__':
    # Display summary for stock_data
    print('Stocks\n')
    # ... YOUR CODE FOR TASK 2 HERE ...
    print(stock_data.info())
    print(stock_data.head())
    print(stock_data.describe())

    # Display summary for benchmark_data
    print('\nBenchmarks\n')
    # ... YOUR CODE FOR TASK 2 HERE ...
    print(benchmark_data.info())
    print(benchmark_data.head())
    print(benchmark_data.describe())

    stock_data.plot(subplots = True, title = "Stock Data");
    plt.show()

    benchmark_data.plot(title="S&P 500");
    plt.show()

    