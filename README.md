# Plot_Stock_Price
# To plot stock price

import matplotlib.pyplot as plt
from pandas_datareader import data

def plot_stock(stock_quote, start_date, end_date):
    
    '''
    
    stock_quote: a list of stock quote you want to plot
    
    start_date: the starting date of stock price data extracted
        please follow the ISO 0861 standard like 'YYYY-MM-DD'
    
    end_date: the last date of stock price data extracted
        please follow the ISO 0861 standard like 'YYYY-MM-DD'
    '''
    
    # Create a figure first
    
    fig = plt.figure(figsize = (20, 10))
    
    # Add an ax to the figure you just created
    ax = fig.add_subplot(1,1,1)
    
    for stock in stock_quote:
        
        # extract data from stock_quote
        stock_data = data.get_data_yahoo(stock, start = start_date, end = end_date)
        
        # plot to stock chart
        ax.plot(stock_data.index, stock_data['Adj Close'], label = stock)
    
        # set x and y label, and also the text properties
    font = {'size': 16}
    
    ax.set_ylabel(stock_data[['Adj Close']].columns[0], fontdict = font)
    
    ax.set_xlabel(stock_data.index.name, fontdict = font)
    
    # only get the date part from df.index
    ax.set_xticklabels(stock_data.index.date , rotation = 50)
    
    # add legend outside the plot
    ax.legend(bbox_to_anchor = (1.1,0.95))
    
    plt.style.use("ggplot")
    
    plt.show()
   
plot_stock(['CRM','AAPL','TWTR'], '2009-01-01','2019-01-01')
