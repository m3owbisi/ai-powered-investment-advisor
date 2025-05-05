import pandas as pd
import numpy as np
import streamlit as st

def project_portfolio_performance(portfolio, initial_investment=10000, years=10, monte_carlo_sims=1000):
    """
    Project the performance of a portfolio over time.
    
    Args:
        portfolio (dict): Portfolio data including expected return and volatility
        initial_investment (float): Initial investment amount
        years (int): Number of years to project
        monte_carlo_sims (int): Number of Monte Carlo simulations to run
        
    Returns:
        dict: Projected performance data
    """
    # Extract portfolio metrics
    expected_return = portfolio['expected_return']
    expected_volatility = portfolio['expected_volatility']
    
    # Generate timeline
    timeline = np.arange(0, years + 1)
    
    # Expected scenario (deterministic compound growth)
    expected_growth = initial_investment * (1 + expected_return) ** timeline
    
    # Optimistic scenario (higher return, same volatility)
    optimistic_return = expected_return * 1.3  # 30% better returns
    optimistic_growth = initial_investment * (1 + optimistic_return) ** timeline
    
    # Pessimistic scenario (lower return, same volatility)
    pessimistic_return = max(expected_return * 0.7, 0.01)  # 30% worse returns, minimum 1%
    pessimistic_growth = initial_investment * (1 + pessimistic_return) ** timeline
    
    # Create DataFrame for the projection
    projection_df = pd.DataFrame({
        'Year': timeline,
        'Expected': expected_growth,
        'Optimistic': optimistic_growth,
        'Pessimistic': pessimistic_growth
    })
    
    # Final values
    final_values = {
        'Expected': expected_growth[-1],
        'Optimistic': optimistic_growth[-1],
        'Pessimistic': pessimistic_growth[-1]
    }
    
    # Monte Carlo simulation (optional, not displayed in basic version)
    # This simulates many possible paths the portfolio might take
    np.random.seed(42)  # For reproducibility
    simulation_results = []
    
    for i in range(monte_carlo_sims):
        # Generate random returns with expected return and volatility
        random_returns = np.random.normal(expected_return, expected_volatility, years)
        # Simulate growth path
        portfolio_value = [initial_investment]
        
        for annual_return in random_returns:
            portfolio_value.append(portfolio_value[-1] * (1 + annual_return))
        
        simulation_results.append(portfolio_value)
    
    # Convert to numpy array for easier calculations
    simulation_array = np.array(simulation_results)
    
    # Calculate percentiles for each year
    percentiles = {
        '5th': np.percentile(simulation_array, 5, axis=0),
        '25th': np.percentile(simulation_array, 25, axis=0),
        '50th': np.percentile(simulation_array, 50, axis=0),
        '75th': np.percentile(simulation_array, 75, axis=0),
        '95th': np.percentile(simulation_array, 95, axis=0)
    }
    
    return {
        'projection_df': projection_df,
        'final_values': final_values,
        'monte_carlo': {
            'simulations': simulation_array,
            'percentiles': percentiles
        }
    }
