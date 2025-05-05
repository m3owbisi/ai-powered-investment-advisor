import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Import custom modules
from risk_assessment import get_risk_profile, get_risk_score
from financial_data import get_market_data, get_stock_data, get_index_data
from portfolio_optimizer import get_optimized_portfolio
from performance_projections import project_portfolio_performance
from educational_content import investment_education
from utils import load_profile_image

# Set page config
st.set_page_config(
    page_title="AI Investment Advisor",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'risk_profile' not in st.session_state:
    st.session_state.risk_profile = None
if 'risk_score' not in st.session_state:
    st.session_state.risk_score = None
if 'portfolio' not in st.session_state:
    st.session_state.portfolio = None
if 'projected_performance' not in st.session_state:
    st.session_state.projected_performance = None
if 'show_questionnaire' not in st.session_state:
    st.session_state.show_questionnaire = False
if 'market_data' not in st.session_state:
    st.session_state.market_data = None
if 'selected_stocks' not in st.session_state:
    st.session_state.selected_stocks = []
if 'education_tab' not in st.session_state:
    st.session_state.education_tab = "Basics"

# Sidebar navigation
st.sidebar.title("AI Investment Advisor")
page = st.sidebar.radio("Navigation", ["Home", "Risk Assessment", "Portfolio Recommendation", "Market Analysis", "Performance Projections", "Education"])

# Home page
if page == "Home":
    st.title("Welcome to AI Investment Advisor")
    st.subheader("Personalized financial recommendations based on your risk profile")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("""
        Our AI-powered platform helps you make informed investment decisions by:
        
        - Assessing your risk tolerance and investment goals
        - Recommending optimized portfolios based on your profile
        - Analyzing market trends and historical data
        - Projecting potential investment performance
        - Providing educational resources on investment strategies
        """)
        
        if st.button("Get Started with Risk Assessment"):
            st.session_state.show_questionnaire = True
            st.rerun()
    
    with col2:
        st.image("https://cdn.jsdelivr.net/gh/feathericons/feather@4.29.0/icons/pie-chart.svg", width=200)
    
    # Recent market trends
    st.subheader("Market Snapshot")
    try:
        index_data = get_index_data(['SPY', 'QQQ', 'IWM'], days=30)
        
        if index_data is not None:
            fig = px.line(
                index_data, x=index_data.index, y=['SPY', 'QQQ', 'IWM'],
                labels={'value': 'Normalized Price', 'variable': 'Index'},
                title='Major Market Indices (Last 30 Days)'
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Market data is currently unavailable. Please try again later.")
    except Exception as e:
        st.error(f"Error loading market data: {str(e)}")

# Risk Assessment page
elif page == "Risk Assessment":
    st.title("Risk Profile Assessment")
    st.write("Let's determine your investment risk profile by answering a few questions.")
    
    risk_profile, risk_score = get_risk_profile()
    
    if risk_profile and risk_score:
        st.session_state.risk_profile = risk_profile
        st.session_state.risk_score = risk_score
        
        st.success(f"Your risk profile has been determined: **{risk_profile}**")
        st.progress(risk_score / 100)
        
        st.write("""
        ### What does this mean?
        
        Your risk profile helps us determine the optimal portfolio allocation that aligns with your risk tolerance and investment goals.
        """)
        
        if st.button("View Portfolio Recommendation"):
            st.rerun()

# Portfolio Recommendation page
elif page == "Portfolio Recommendation":
    st.title("Portfolio Recommendation")
    
    if st.session_state.risk_profile is None:
        st.warning("Please complete the risk assessment first.")
        if st.button("Go to Risk Assessment"):
            st.rerun()
    else:
        st.write(f"Based on your **{st.session_state.risk_profile}** risk profile, here's our recommended portfolio allocation:")
        
        try:
            portfolio = get_optimized_portfolio(st.session_state.risk_profile)
            st.session_state.portfolio = portfolio
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                fig = px.pie(
                    values=portfolio['allocation'],
                    names=portfolio['asset_class'],
                    title='Recommended Portfolio Allocation',
                    hole=0.4,
                )
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                st.subheader("Portfolio Details")
                st.write(f"Expected Annual Return: **{portfolio['expected_return']:.2%}**")
                st.write(f"Expected Volatility: **{portfolio['expected_volatility']:.2%}**")
                st.write(f"Sharpe Ratio: **{portfolio['sharpe_ratio']:.2f}**")
            
            st.subheader("Suggested Assets")
            allocation_df = pd.DataFrame({
                'Asset Class': portfolio['asset_class'],
                'Allocation (%)': [f"{int(x * 100)}%" for x in portfolio['allocation']],
                'Example Ticker': portfolio['example_tickers'],
                'Description': portfolio['descriptions']
            })
            st.dataframe(allocation_df, hide_index=True)
            
            st.info("This is a high-level asset allocation. For a more detailed portfolio with specific securities, please consult with a financial advisor.")
            
        except Exception as e:
            st.error(f"Error generating portfolio recommendation: {str(e)}")

# Market Analysis page
elif page == "Market Analysis":
    st.title("Market Analysis")
    
    st.subheader("Analyze Historical Market Data")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        ticker_input = st.text_input("Enter ticker symbols (comma-separated)", "AAPL,MSFT,GOOGL")
    
    with col2:
        period = st.selectbox("Select time period", ["1 Month", "3 Months", "6 Months", "1 Year", "3 Years", "5 Years"])
    
    if ticker_input:
        tickers = [ticker.strip() for ticker in ticker_input.split(',')]
        st.session_state.selected_stocks = tickers
        
        period_days = {
            "1 Month": 30,
            "3 Months": 90,
            "6 Months": 180,
            "1 Year": 365,
            "3 Years": 365 * 3,
            "5 Years": 365 * 5
        }
        
        try:
            with st.spinner('Fetching market data...'):
                market_data = get_stock_data(tickers, days=period_days[period])
                st.session_state.market_data = market_data
            
            if market_data is not None:
                # Price chart
                fig = px.line(
                    market_data['normalized'], 
                    labels={'value': 'Normalized Price', 'variable': 'Stock'},
                    title=f'Comparative Stock Performance ({period})'
                )
                st.plotly_chart(fig, use_container_width=True)
                
                # Returns chart
                fig_return = px.bar(
                    market_data['returns'], 
                    labels={'value': 'Total Return (%)', 'variable': 'Stock'},
                    title=f'Total Returns ({period})'
                )
                st.plotly_chart(fig_return, use_container_width=True)
                
                # Volatility and metrics
                st.subheader("Risk & Return Metrics")
                metrics_df = pd.DataFrame({
                    'Stock': tickers,
                    'Total Return (%)': [f"{market_data['returns'].iloc[-1][ticker]:.2f}%" for ticker in tickers],
                    'Volatility (%)': [f"{market_data['volatility'][ticker]:.2f}%" for ticker in tickers],
                    'Sharpe Ratio': [f"{market_data['sharpe'][ticker]:.2f}" for ticker in tickers],
                })
                st.dataframe(metrics_df, hide_index=True)
                
                # Correlation matrix
                st.subheader("Correlation Matrix")
                fig_corr = px.imshow(
                    market_data['correlation'],
                    text_auto=True,
                    color_continuous_scale='RdBu_r',
                    title='Stock Price Correlation'
                )
                st.plotly_chart(fig_corr, use_container_width=True)
            else:
                st.warning("No data available for the selected tickers or time period. Please check your inputs and try again.")
        except Exception as e:
            st.error(f"Error analyzing market data: {str(e)}")

# Performance Projections page
elif page == "Performance Projections":
    st.title("Performance Projections")
    
    if st.session_state.portfolio is None:
        st.warning("Please complete the portfolio recommendation first.")
        if st.button("Go to Portfolio Recommendation"):
            st.rerun()
    else:
        st.write("See how your recommended portfolio might perform over time.")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            initial_investment = st.number_input("Initial Investment ($)", min_value=1000, max_value=10000000, value=10000, step=1000)
        
        with col2:
            time_horizon = st.slider("Investment Time Horizon (Years)", min_value=1, max_value=30, value=10)
        
        try:
            projected_performance = project_portfolio_performance(
                st.session_state.portfolio,
                initial_investment=initial_investment,
                years=time_horizon
            )
            st.session_state.projected_performance = projected_performance
            
            # Performance projection chart
            fig = px.line(
                projected_performance['projection_df'],
                x='Year',
                y=['Expected', 'Optimistic', 'Pessimistic'],
                labels={'value': 'Portfolio Value ($)', 'variable': 'Scenario'},
                title=f'Projected Portfolio Performance Over {time_horizon} Years'
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Final values
            st.subheader("Projected Final Values")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    "Expected Scenario", 
                    f"${projected_performance['final_values']['Expected']:,.2f}", 
                    f"{((projected_performance['final_values']['Expected'] / initial_investment) - 1) * 100:.1f}%"
                )
            
            with col2:
                st.metric(
                    "Optimistic Scenario", 
                    f"${projected_performance['final_values']['Optimistic']:,.2f}", 
                    f"{((projected_performance['final_values']['Optimistic'] / initial_investment) - 1) * 100:.1f}%"
                )
            
            with col3:
                st.metric(
                    "Pessimistic Scenario", 
                    f"${projected_performance['final_values']['Pessimistic']:,.2f}", 
                    f"{((projected_performance['final_values']['Pessimistic'] / initial_investment) - 1) * 100:.1f}%"
                )
            
            # Disclaimer
            st.info("""
            **Disclaimer**: These projections are based on historical data and assumptions about future market conditions. 
            Actual results may vary significantly. Past performance is not indicative of future results.
            """)
            
        except Exception as e:
            st.error(f"Error generating performance projections: {str(e)}")

# Education page
elif page == "Education":
    st.title("Investment Education")
    
    education_tabs = investment_education()

# Footer
st.markdown("""
---
*This AI Investment Advisor is for educational purposes only. It does not constitute financial advice, and you should consult with a qualified financial advisor before making investment decisions.*
""")
