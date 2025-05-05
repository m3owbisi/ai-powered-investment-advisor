import pandas as pd
import numpy as np
from sklearn.covariance import LedoitWolf
import yfinance as yf
from datetime import datetime, timedelta

def get_optimized_portfolio(risk_profile):
    """
    Generate an optimized portfolio based on the user's risk profile.
    
    Args:
        risk_profile (str): The user's risk profile (Conservative, Moderately Conservative, Moderate, Moderately Aggressive, Aggressive)
        
    Returns:
        dict: Portfolio allocation, expected returns, volatility, and more
    """
    # Define asset allocation based on risk profile
    allocation_maps = {
        "Conservative": {
            "US Bonds": 0.5,
            "International Bonds": 0.15,
            "US Large Cap": 0.15,
            "US Mid/Small Cap": 0.05,
            "International Equity": 0.1,
            "Real Estate": 0.05,
            "Cash": 0.0
        },
        "Moderately Conservative": {
            "US Bonds": 0.40,
            "International Bonds": 0.10,
            "US Large Cap": 0.25,
            "US Mid/Small Cap": 0.05,
            "International Equity": 0.15,
            "Real Estate": 0.05,
            "Cash": 0.0
        },
        "Moderate": {
            "US Bonds": 0.25,
            "International Bonds": 0.10,
            "US Large Cap": 0.30,
            "US Mid/Small Cap": 0.10,
            "International Equity": 0.20,
            "Real Estate": 0.05,
            "Cash": 0.0
        },
        "Moderately Aggressive": {
            "US Bonds": 0.15,
            "International Bonds": 0.05,
            "US Large Cap": 0.35,
            "US Mid/Small Cap": 0.15,
            "International Equity": 0.25,
            "Real Estate": 0.05,
            "Cash": 0.0
        },
        "Aggressive": {
            "US Bonds": 0.05,
            "International Bonds": 0.05,
            "US Large Cap": 0.40,
            "US Mid/Small Cap": 0.15,
            "International Equity": 0.30,
            "Real Estate": 0.05,
            "Cash": 0.0
        }
    }
    
    # Get the allocation for the user's risk profile
    allocation = allocation_maps.get(risk_profile, allocation_maps["Moderate"])
    
    # Example ETFs for each asset class
    example_tickers = {
        "US Bonds": "AGG",  # iShares Core U.S. Aggregate Bond ETF
        "International Bonds": "BNDX",  # Vanguard Total International Bond ETF
        "US Large Cap": "VTI",  # Vanguard Total Stock Market ETF
        "US Mid/Small Cap": "IJR",  # iShares Core S&P Small-Cap ETF
        "International Equity": "VXUS",  # Vanguard Total International Stock ETF
        "Real Estate": "VNQ",  # Vanguard Real Estate ETF
        "Cash": "SHV"  # iShares Short Treasury Bond ETF
    }
    
    # Descriptions for each asset class
    descriptions = {
        "US Bonds": "U.S. investment-grade bonds for stable income and lower volatility",
        "International Bonds": "Non-U.S. bonds for diversification and yield",
        "US Large Cap": "Large U.S. companies for growth and stability",
        "US Mid/Small Cap": "Smaller U.S. companies with higher growth potential",
        "International Equity": "Non-U.S. stocks for global diversification",
        "Real Estate": "REITs and real estate securities for income and inflation protection",
        "Cash": "Short-term treasury securities for capital preservation"
    }
    
    # Calculate expected returns and volatility
    # These are simplified assumptions based on historical data
    expected_returns = {
        "US Bonds": 0.03,  # 3%
        "International Bonds": 0.035,  # 3.5%
        "US Large Cap": 0.08,  # 8%
        "US Mid/Small Cap": 0.09,  # 9%
        "International Equity": 0.075,  # 7.5%
        "Real Estate": 0.06,  # 6%
        "Cash": 0.015  # 1.5%
    }
    
    expected_volatility = {
        "US Bonds": 0.05,  # 5%
        "International Bonds": 0.06,  # 6%
        "US Large Cap": 0.15,  # 15%
        "US Mid/Small Cap": 0.20,  # 20%
        "International Equity": 0.18,  # 18%
        "Real Estate": 0.17,  # 17%
        "Cash": 0.01  # 1%
    }
    
    # Calculate portfolio expected return and volatility
    portfolio_return = sum(allocation[asset] * expected_returns[asset] for asset in allocation)
    
    # Simplified correlation matrix (in practice, this would be calculated from historical data)
    # This is a very basic approximation
    correlation_matrix = np.array([
        [1.0, 0.8, 0.2, 0.2, 0.2, 0.3, 0.1],  # US Bonds
        [0.8, 1.0, 0.2, 0.2, 0.3, 0.3, 0.1],  # International Bonds
        [0.2, 0.2, 1.0, 0.8, 0.8, 0.7, 0.0],  # US Large Cap
        [0.2, 0.2, 0.8, 1.0, 0.7, 0.7, 0.0],  # US Mid/Small Cap
        [0.2, 0.3, 0.8, 0.7, 1.0, 0.6, 0.0],  # International Equity
        [0.3, 0.3, 0.7, 0.7, 0.6, 1.0, 0.1],  # Real Estate
        [0.1, 0.1, 0.0, 0.0, 0.0, 0.1, 1.0]   # Cash
    ])
    
    volatility_vector = np.array([expected_volatility[asset] for asset in allocation])
    allocation_vector = np.array([allocation[asset] for asset in allocation])
    
    # Convert correlation matrix to covariance matrix
    cov_matrix = np.outer(volatility_vector, volatility_vector) * correlation_matrix
    
    # Calculate portfolio volatility
    portfolio_volatility = np.sqrt(allocation_vector.T @ cov_matrix @ allocation_vector)
    
    # Calculate Sharpe ratio (assuming risk-free rate of 1.5%)
    risk_free_rate = 0.015
    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility
    
    # Prepare the result
    result = {
        'risk_profile': risk_profile,
        'asset_class': list(allocation.keys()),
        'allocation': list(allocation.values()),
        'example_tickers': [example_tickers[asset] for asset in allocation],
        'descriptions': [descriptions[asset] for asset in allocation],
        'expected_return': portfolio_return,
        'expected_volatility': portfolio_volatility,
        'sharpe_ratio': sharpe_ratio
    }
    
    return result

def optimize_portfolio_monte_carlo(risk_profile, num_simulations=10000):
    """
    Advanced optimization using Monte Carlo simulation.
    Note: This function is provided for reference but not used in the current app.
    In a production environment, this could replace the basic allocation approach.
    
    Args:
        risk_profile (str): The user's risk profile
        num_simulations (int): Number of Monte Carlo simulations
        
    Returns:
        dict: Optimized portfolio allocation and metrics
    """
    # This would be a more sophisticated implementation using Monte Carlo simulation
    # to find an optimal portfolio on the efficient frontier.
    
    # For the purpose of the example app, we use the simpler approach above.
    # In a real implementation, this would involve:
    # 1. Getting historical return data for each asset class
    # 2. Calculating covariance matrix
    # 3. Generating random portfolio weights many times
    # 4. Finding the portfolio that maximizes Sharpe ratio for the given risk profile
    
    # This would be implemented if requested as an enhancement
    pass
