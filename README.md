How to Plot Your Stock Price
============================

To plot stock price

  Hello everyone, this is my first project, which is used for ploting several stock charts on the same plot, so we can easily compare trends of different stock over time. I love finance. In particular with financial perspective, I can comfortably understand how the world runs, and I also believe, to some extend, our world is capital-driven.

  This is just my first project, after 3-month study of Python. If you have any problems, good suggestions or even cool ideas, please feel free to let me know and send me an email via mankawa343134328@gmail.com. I am very looking forward to see your valuable comments

Thank you so much, and now let's enjoy coding!

## Problem
  When I was reading stock charts, I found that some of the platforms such as WSJ had already standardized their selections of trading period to 1-year, 3-year and 5-year period. What if I want to view a stock chart on a very special or non-standard trading period? For instance, I want to view stock price trend of Salesforce, starting from June to August, after the annoucement of the acquisition of Tableau by Salesforce. This will help investors analyze how investors digest this piece of news even 2 to 3 months after the deal announced.
  
## Solution 
  This incentive really drives me to create a chart on which the trading period can be fully **customized** by our investors.
  Actually, the work of writting these codes did not take me too long. In my estimation, it took simply 3 - 4 nights. After all, these are all simple codes. I used my own spare time and coffee time (I am extremely fond of and addicited to coffee, T-T) to write these codes.

## Code
```python
# import matplotlib to plot the stock we pick
import matplotlib.pyplot as plt

# import pandas_datareader for getting the stock price data from Yahoo
from pandas_datareader import data

# define a function 
def plot_stock(stock_quote, start_date, end_date):
    
    '''
    stock_quote: a list of stock quote you want to plot
        e.g. 'CRM' for Salesforce for  a single stock, you can pass a list which contains multiple stock like     ['AAPL','CRM','TSLA']
    
    start_date: the first trade date on which stock price data will be downloaded 
        please follow the ISO 0861 format - 'YYYY-MM-DD'
    
    end_date: the last trade date on which stock price data will be downloaded
        please follow the ISO 0861 format - 'YYYY-MM-DD'
    '''
    
    # Create a figure first
    fig = plt.figure(figsize = (20, 10))
    
    # Add an ax to the figure you just created
    ax = fig.add_subplot(1,1,1)
    
    for stock in stock_quote:
        
        # download data from by passing stock quote
        # (e.g 'CRM' for Salesforce, start_date = '2019-01-01', end_data = '2019-10-01')
        stock_data = data.get_data_yahoo(stock, start = start_date, end = end_date)
        
        # plot to stock chart
        ax.plot(stock_data.index, stock_data['Adj Close'], label = stock)
    
    # set x and y label, and also the text properties：fontszie
    font = {'size': 16}
    
    # Set the  ylabel of the chart, and fontsize
    ax.set_ylabel(stock_data[['Adj Close']].columns[0], fontdict = font)
    
    ax.set_xlabel(stock_data.index.name, fontdict = font)
    
    # only get the date part from df.index
    ax.set_xticklabels(stock_data.index.date , rotation = 50)
    
    # add legend outside the plot
    ax.legend(bbox_to_anchor = (1.1,0.95))
    
    # set the chart style, I love ggplot, how about you.
    plt.style.use("ggplot")
    
    plt.show()
   
plot_stock(['CRM','AAPL','TWTR'], '2009-01-01','2019-01-01')

```
  You can just copy these codes and have a try in your Python IDE, please make sure that you have installed
both matplotlib and pandas_datareader. If not, you can just simply copy and paste this command to your Mac terminal

```bat
pip install matplotlib
pip install pandas_datareader 
```

  Here are the results after running the python scripts

![Result](https://raw.githubusercontent.com/kwlwman2/Plot_Stock_Price/master/Result.png)

## Limitations & Improvement
  The chart is very easy to read. However, and I will try to add more powerful functions like interactive interface, and scroll bar of adjusting the days for moving average, which could smooth out those swings and help us focus on long-term stock trend. Please stay tuned for my Github. Thank you so much for your patience and time.
