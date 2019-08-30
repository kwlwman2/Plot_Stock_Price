# import matplotlib to plot the stock we pick
import matplotlib.pyplot as plt

# import pandas_datareader for getting the stock price data from Yahoo
from pandas_datareader import data

# define a function 
def plot_stock(stock_quote, start_date, end_date):
    
    '''
    stock_quote: a list of stock quote you want to plot
        e.g. 'CRM' for Salesforce for  a single stock, you can pass a list which contains multiple stock like ['AAPL','CRM','TSLA']
    
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
