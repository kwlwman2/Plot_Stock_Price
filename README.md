How to Plot Your Stock Price
=========================

To plot stock price

  Hello everyone, this is my first project, which is used for ploting several stock charts on the same plot, so we can easily compare trends of different stock over time. I love finance. In particular with finance's perspective, I can comfortably under stand how the world runs, and I also believe, to some extend, our world is capital-drive.

  This is just my first project, after 3-month study of Python. If you have anything problems, good suggestions and cool ideas, please feel free to let me know and drop me an email via mankawa343134328@gmail.com. I am very looking forward to see your valuable comments

Thank you so much and now let's enjoy coding!

## Problem
  When I was reading stock chart, I found that some of the platform such as Futu, Bloomberg and WSJ, which have already standardized their selections of trading period to 1-year, 3-year and 5-year period. What if I want to view a stock chart, on a very specific trading period. For instance, I want to view stock price trend of Salesforce, starting from June to August because of Salesforce annouce the acquisition of Tableau. 
  
## Solution 
  This incentive really drives me to create a chart on which the trading period can be fully *customized* by our investors.
  
  Actually, the works of writting these codes did not take me too long, I estimated just 3 - 4 nights after all these are all simple codes. I used my own spare time and coffee time (I am extremely fond of and addicited to coffee, T-T) to write these codes. 

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
'''
# you can just copy this code and have a try in your Python IDE, please make sure that you have installed
matplotlib and pandas_datareader
'''
```
![Result](https://raw.githubusercontent.com/kwlwman2/Plot_Stock_Price/master/Result.png)
