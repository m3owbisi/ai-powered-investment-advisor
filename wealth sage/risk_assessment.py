import streamlit as st
import numpy as np

def get_risk_profile():
    """
    Gather user responses to risk assessment questions and calculate risk profile.
    
    Returns:
        tuple: (risk_profile, risk_score) where risk_profile is a string and risk_score is a float (0-100)
    """
    if st.session_state.risk_profile is not None and not st.session_state.show_questionnaire:
        return st.session_state.risk_profile, st.session_state.risk_score
    
    st.session_state.show_questionnaire = True
    
    st.write("Please answer the following questions to help us determine your risk tolerance.")
    
    # Question 1: Investment timeline
    q1 = st.selectbox(
        "1. What is your investment time horizon?",
        ["Less than 1 year", "1-3 years", "3-5 years", "5-10 years", "More than 10 years"],
        index=2
    )
    
    # Question 2: Financial goals
    q2 = st.selectbox(
        "2. What is your primary financial goal?",
        ["Preserving capital (minimal risk)", "Income generation", "Balanced growth and income", "Long-term growth", "Aggressive growth (maximum returns)"],
        index=2
    )
    
    # Question 3: Market downturn reaction
    q3 = st.selectbox(
        "3. How would you react if your investment portfolio lost 20% of its value in a month?",
        ["Sell everything immediately", "Sell a portion to cut losses", "Do nothing and wait it out", "Evaluate and possibly rebalance", "Buy more to take advantage of lower prices"],
        index=2
    )
    
    # Question 4: Investment knowledge
    q4 = st.selectbox(
        "4. How would you rate your investment knowledge and experience?",
        ["No knowledge", "Limited knowledge", "Moderate knowledge", "Good knowledge", "Expert knowledge"],
        index=2
    )
    
    # Question 5: Risk vs. Return preference
    q5 = st.select_slider(
        "5. Which statement best describes your attitude toward investment risk and return?",
        options=["I prefer guaranteed returns, even if they're small", 
                "I prefer stable investments with moderate returns", 
                "I'm comfortable with some fluctuations for better returns", 
                "I can accept significant fluctuations for potentially high returns", 
                "I'm seeking maximum returns and can handle extreme volatility"]
    )
    
    # Question 6: Income stability
    q6 = st.selectbox(
        "6. How stable is your current income source?",
        ["Very unstable", "Somewhat unstable", "Moderately stable", "Stable", "Very stable"],
        index=2
    )
    
    # Question 7: Emergency fund
    q7 = st.selectbox(
        "7. Do you have an emergency fund that could cover your expenses for at least 3-6 months?",
        ["No emergency fund", "Less than 1 month", "1-3 months", "3-6 months", "More than 6 months"],
        index=2
    )
    
    # Question 8: Portfolio allocation preference
    q8 = st.select_slider(
        "8. Which portfolio allocation are you most comfortable with?",
        options=["80% Bonds, 20% Stocks", 
                "60% Bonds, 40% Stocks", 
                "50% Bonds, 50% Stocks", 
                "40% Bonds, 60% Stocks", 
                "20% Bonds, 80% Stocks"]
    )
    
    if st.button("Calculate My Risk Profile"):
        risk_score = get_risk_score(q1, q2, q3, q4, q5, q6, q7, q8)
        risk_profile = get_profile_from_score(risk_score)
        
        st.session_state.risk_profile = risk_profile
        st.session_state.risk_score = risk_score
        st.session_state.show_questionnaire = False
        
        return risk_profile, risk_score
    
    return None, None

def get_risk_score(q1, q2, q3, q4, q5, q6, q7, q8):
    """
    Calculate a risk score (0-100) based on questionnaire responses.
    
    Args:
        q1-q8: Responses to the risk assessment questions
        
    Returns:
        float: Risk score between 0 and 100
    """
    # Map responses to numerical scores (1-5, with 5 being highest risk tolerance)
    
    # Question 1: Investment timeline
    q1_map = {
        "Less than 1 year": 1,
        "1-3 years": 2,
        "3-5 years": 3,
        "5-10 years": 4,
        "More than 10 years": 5
    }
    
    # Question 2: Financial goals
    q2_map = {
        "Preserving capital (minimal risk)": 1,
        "Income generation": 2,
        "Balanced growth and income": 3,
        "Long-term growth": 4,
        "Aggressive growth (maximum returns)": 5
    }
    
    # Question 3: Market downturn reaction
    q3_map = {
        "Sell everything immediately": 1,
        "Sell a portion to cut losses": 2,
        "Do nothing and wait it out": 3,
        "Evaluate and possibly rebalance": 4,
        "Buy more to take advantage of lower prices": 5
    }
    
    # Question 4: Investment knowledge
    q4_map = {
        "No knowledge": 1,
        "Limited knowledge": 2,
        "Moderate knowledge": 3,
        "Good knowledge": 4,
        "Expert knowledge": 5
    }
    
    # Question 5: Risk vs. Return preference
    q5_map = {
        "I prefer guaranteed returns, even if they're small": 1,
        "I prefer stable investments with moderate returns": 2,
        "I'm comfortable with some fluctuations for better returns": 3,
        "I can accept significant fluctuations for potentially high returns": 4,
        "I'm seeking maximum returns and can handle extreme volatility": 5
    }
    
    # Question 6: Income stability
    q6_map = {
        "Very unstable": 1,
        "Somewhat unstable": 2,
        "Moderately stable": 3,
        "Stable": 4,
        "Very stable": 5
    }
    
    # Question 7: Emergency fund
    q7_map = {
        "No emergency fund": 1,
        "Less than 1 month": 2,
        "1-3 months": 3,
        "3-6 months": 4,
        "More than 6 months": 5
    }
    
    # Question 8: Portfolio allocation preference
    q8_map = {
        "80% Bonds, 20% Stocks": 1,
        "60% Bonds, 40% Stocks": 2,
        "50% Bonds, 50% Stocks": 3,
        "40% Bonds, 60% Stocks": 4,
        "20% Bonds, 80% Stocks": 5
    }
    
    # Calculate weighted score
    weights = {
        'q1': 1.5,  # Time horizon is important
        'q2': 1.0,
        'q3': 1.5,  # Reaction to market downturn is important
        'q4': 0.8,
        'q5': 1.5,  # Risk vs return preference is important
        'q6': 0.8,
        'q7': 1.0,
        'q8': 1.2   # Portfolio preference is fairly important
    }
    
    # Calculate weighted score
    score = (q1_map[q1] * weights['q1'] +
             q2_map[q2] * weights['q2'] +
             q3_map[q3] * weights['q3'] +
             q4_map[q4] * weights['q4'] +
             q5_map[q5] * weights['q5'] +
             q6_map[q6] * weights['q6'] +
             q7_map[q7] * weights['q7'] +
             q8_map[q8] * weights['q8'])
    
    # Normalize to 0-100 scale
    max_possible_score = sum(weights.values()) * 5
    normalized_score = (score / max_possible_score) * 100
    
    return normalized_score

def get_profile_from_score(score):
    """
    Map a risk score to a risk profile category.
    
    Args:
        score (float): Risk score between 0 and 100
        
    Returns:
        str: Risk profile category
    """
    if score < 20:
        return "Conservative"
    elif score < 40:
        return "Moderately Conservative"
    elif score < 60:
        return "Moderate"
    elif score < 80:
        return "Moderately Aggressive"
    else:
        return "Aggressive"
