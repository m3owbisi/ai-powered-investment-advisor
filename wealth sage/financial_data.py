import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta

def get_market_data(tickers, days=365):
    """
    Fetch historical market data for the specified tickers over the specified period.
    
    Args:
        tickers (list): List of ticker symbols
        days (int): Number of days to look back
        
    Returns:
        dict: Dictionary containing various market data metrics
    """
    try:
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
        
        # Fetch data
        data = yf.download(tickers, start=start_date, end=end_date)
        
        if data.empty:
            return None
        
        # Extract closing prices
        prices = data['Adj Close'].copy()
        
        # Calculate daily returns
        daily_returns = prices.pct_change().dropna()
        
        # Calculate cumulative returns
        cumulative_returns = (1 + daily_returns).cumprod() - 1
        
        # Calculate volatility (annualized standard deviation of returns)
        volatility = daily_returns.std() * np.sqrt(252) * 100
        
        # Calculate Sharpe ratio (assuming risk-free rate of 0% for simplicity)
        sharpe = (daily_returns.mean() * 252) / (daily_returns.std() * np.sqrt(252))
        
        # Normalize prices for comparison (set initial price to 100)
        normalized = prices / prices.iloc[0] * 100
        
        # Calculate correlation matrix
        correlation = daily_returns.corr()
        
        return {
            'prices': prices,
            'daily_returns': daily_returns,
            'cumulative_returns': cumulative_returns,
            'normalized': normalized,
            'volatility': volatility,
            'sharpe': sharpe,
            'correlation': correlation,
            'returns': cumulative_returns * 100  # Convert to percentage
        }
    except Exception as e:
        print(f"Error fetching market data: {str(e)}")
        return None

def get_stock_data(tickers, days=365):
    """
    Fetch and process historical stock data for the specified tickers.
    This is a wrapper around get_market_data for stock-specific data.
    
    Args:
        tickers (list): List of stock ticker symbols
        days (int): Number of days to look back
        
    Returns:
        dict: Dictionary containing various stock data metrics
    """
    return get_market_data(tickers, days)

def get_index_data(indices=['SPY', 'QQQ', 'IWM'], days=30):
    """
    Fetch and process index data for market overview.
    
    Args:
        indices (list): List of index ETF symbols
        days (int): Number of days to look back
        
    Returns:
        pandas.DataFrame: Normalized price data for the indices
    """
    try:
        market_data = get_market_data(indices, days)
        if market_data:
            return market_data['normalized']
        return None
    except Exception as e:
        print(f"Error fetching index data: {str(e)}")
        return None
