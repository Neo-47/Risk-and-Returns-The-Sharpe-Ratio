from prepare_data import stock_data, benchmark_data
import matplotlib.pyplot as plt
import numpy as np

"""
The inputs for the Sharpe Ratio: Starting with Daily Stock Returns

The Sharpe Ratio uses the difference in returns between the two investment opportunities under consideration.

However, our data show the historical value of each investment, not the return. 
To calculate the return, we need to calculate the percentage change in value from one day to the next. 

"""

# calculate daily stock_data returns
stock_returns = stock_data.pct_change()


# The pandas method .pct_change() calculates the relative change
# from one value to the next in a DataFrame.
stock_returns.plot(subplots = True)
plt.show()

# summarize the daily returns
print(stock_returns.describe())


# calculate daily benchmark_data returns
sp_returns = benchmark_data['S&P 500'].pct_change()

# plot the daily returns
sp_returns.plot();
plt.show()

# summarize the daily returns
print(sp_returns.describe())


"""
Calculating Excess Returns for Amazon and Facebook vs. S&P 500

Next, we need to calculate the relative performance of stocks vs. the S&P 500 benchmark.
This is calculated as the difference in returns between stock_returns and sp_returns for each day.

"""


# calculate the difference in daily returns
excess_returns = stock_returns.sub(sp_returns, axis = 0)

# plot the excess_returns
excess_returns.plot(subplots = True)

# summarize the excess_returns
print(excess_returns.describe())



"""

The Sharpe Ratio, Step 1: The Average Difference in Daily Returns Stocks vs S&P 500

Now we can finally start computing the Sharpe Ratio.
First we need to calculate the average of the excess_returns. 
This tells us how much more or less the investment yields per day compared to the benchmark.

"""

# calculate the mean of excess_returns 
avg_excess_return = excess_returns.mean()

# plot avg_excess_returns
avg_excess_return.plot.bar(title = "Mean of the Return Difference")
plt.show()



"""

The Sharpe Ratio, Step 2: Standard Deviation of the Return Difference

t looks like there was quite a bit of a difference between average daily returns for Amazon and Facebook.

Next, we calculate the standard deviation of the excess_returns.
This shows us the amount of risk an investment in the stocks implies as compared to an investment in the S&P 500.

"""

# calculate the standard deviations
sd_excess_return = excess_returns.std()

# plot the standard deviations
sd_excess_return.plot.bar(title = "Standard Deviation of the Return Difference");
plt.show()


""" 

Putting it all together

Now we just need to compute the ratio of avg_excess_returns and sd_excess_returns.
The result is now finally the Sharpe ratio and indicates how much more (or less)
return the investment opportunity under consideration yields per unit of risk.

"""

# calculate the daily sharpe ratio
daily_sharpe_ratio = avg_excess_return.div(sd_excess_return)

# annualize the sharpe ratio
annual_factor = np.sqrt(252)
annual_sharpe_ratio = daily_sharpe_ratio.mul(annual_factor)

# plot the annualized sharpe ratio
annual_sharpe_ratio.plot.bar(title = "Annualized Sharpe Ratio: Stocks vs S&P 500");
plt.show()


