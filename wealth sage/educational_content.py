import streamlit as st

def investment_education():
    """
    Provide educational content on investment strategies and concepts.
    
    Returns:
        tabs: Streamlit tabs widget with educational content
    """
    st.write("Learn about investment strategies and concepts to make more informed decisions.")
    
    # Create tabs for different educational topics
    tabs = st.tabs(["Investment Basics", "Asset Classes", "Risk Management", "Portfolio Strategies", "Market Analysis"])
    
    # Investment Basics tab
    with tabs[0]:
        st.header("Investment Basics")
        
        st.subheader("What is Investing?")
        st.write("""
        Investing means allocating resources (usually money) with the expectation of generating income or profit over time.
        Unlike saving, which focuses on preserving capital, investing aims to grow your wealth by putting money to work.
        """)
        
        st.subheader("The Power of Compound Interest")
        st.write("""
        Compound interest is often called the 'eighth wonder of the world.' It's the process where the interest you earn
        on your investment also earns interest over time, creating exponential growth.
        
        For example, $10,000 invested at 7% annual return will grow to:
        - $19,672 after 10 years
        - $38,697 after 20 years
        - $76,123 after 30 years
        
        This demonstrates why starting early is one of the most important investment strategies.
        """)
        
        st.subheader("Risk vs. Return")
        st.write("""
        Generally, investments with higher potential returns come with higher risks. Understanding this relationship
        is fundamental to building a portfolio aligned with your goals and risk tolerance.
        
        - Low risk, low return: Cash, CDs, Treasury bills
        - Medium risk, medium return: Bonds, dividend stocks, REITs
        - High risk, high return: Growth stocks, emerging markets, cryptocurrencies
        """)
        
        st.subheader("Time Horizon")
        st.write("""
        Your investment time horizon—how long you plan to hold investments before needing the money—should
        significantly influence your investment strategy.
        
        - Short-term (0-3 years): Focus on capital preservation and liquidity
        - Medium-term (3-10 years): Balanced approach with moderate growth and protection
        - Long-term (10+ years): Greater focus on growth assets like stocks
        """)
    
    # Asset Classes tab
    with tabs[1]:
        st.header("Asset Classes")
        
        st.subheader("Stocks (Equities)")
        st.write("""
        Stocks represent ownership in a company. When you buy a stock, you become a shareholder
        and own a small piece of that business.
        
        **Types of Stocks:**
        - Large-cap: Market capitalization over $10 billion (e.g., Apple, Microsoft)
        - Mid-cap: $2-10 billion market cap
        - Small-cap: $300 million to $2 billion market cap
        - Growth stocks: Companies expected to grow faster than the market
        - Value stocks: Companies trading below their intrinsic value
        - Dividend stocks: Companies that regularly distribute part of their earnings to shareholders
        """)
        
        st.subheader("Bonds (Fixed Income)")
        st.write("""
        Bonds are debt securities where you lend money to an entity (government, municipality, corporation)
        in exchange for interest payments and the return of the bond's face value when it matures.
        
        **Types of Bonds:**
        - Government bonds: Issued by national governments (e.g., U.S. Treasury bonds)
        - Municipal bonds: Issued by states, cities, or counties
        - Corporate bonds: Issued by companies
        - Investment-grade bonds: Higher credit quality, lower risk and yield
        - High-yield (junk) bonds: Lower credit quality, higher risk and yield
        """)
        
        st.subheader("Cash & Cash Equivalents")
        st.write("""
        These are liquid assets that can be quickly converted to cash with minimal or no loss of value.
        
        **Examples:**
        - Savings accounts
        - Money market funds
        - Treasury bills
        - Certificates of deposit (CDs)
        """)
        
        st.subheader("Real Estate")
        st.write("""
        Real estate investments involve purchasing property or investing in real estate securities like REITs.
        
        **Types of Real Estate Investments:**
        - Direct ownership (residential or commercial property)
        - Real Estate Investment Trusts (REITs)
        - Real estate mutual funds or ETFs
        - Real estate crowdfunding
        """)
        
        st.subheader("Alternative Investments")
        st.write("""
        Alternative investments fall outside traditional asset classes.
        
        **Examples:**
        - Commodities (gold, oil, agricultural products)
        - Private equity
        - Hedge funds
        - Collectibles (art, wine, antiques)
        - Cryptocurrencies
        """)
    
    # Risk Management tab
    with tabs[2]:
        st.header("Risk Management")
        
        st.subheader("Types of Investment Risk")
        st.write("""
        Understanding the different types of risk can help you build a more resilient portfolio:
        
        - **Market risk**: The risk that the entire market will decline, affecting most securities
        - **Inflation risk**: The risk that inflation will erode the purchasing power of your investments
        - **Interest rate risk**: The risk that changes in interest rates will impact investment values
        - **Credit risk**: The risk that a bond issuer will default on their payments
        - **Liquidity risk**: The risk of not being able to sell an investment quickly without a significant loss
        - **Concentration risk**: The risk of having too much exposure to a single investment or sector
        """)
        
        st.subheader("Diversification")
        st.write("""
        Diversification is one of the most powerful risk management strategies. By spreading investments across different
        asset classes, sectors, geographies, and time horizons, you can reduce the impact of poor performance in any single area.
        
        **Ways to Diversify:**
        - Across asset classes (stocks, bonds, real estate, etc.)
        - Within asset classes (different sectors, company sizes, etc.)
        - Geographically (domestic and international)
        - By investment style (growth, value, income)
        - Through time (dollar-cost averaging)
        """)
        
        st.subheader("Asset Allocation")
        st.write("""
        Asset allocation—the distribution of investments across different asset categories—is a critical aspect
        of managing risk and optimizing returns based on your goals and risk tolerance.
        
        **Key Considerations:**
        - Your time horizon
        - Risk tolerance
        - Financial goals
        - Current financial situation
        """)
        
        st.subheader("Rebalancing")
        st.write("""
        Over time, some investments will grow faster than others, causing your portfolio to drift from its target allocation.
        Rebalancing involves periodically buying and selling assets to maintain your desired asset allocation.
        
        **Rebalancing Strategies:**
        - Calendar-based (e.g., quarterly, annually)
        - Threshold-based (when allocations drift by a certain percentage)
        - Combination of both approaches
        """)
    
    # Portfolio Strategies tab
    with tabs[3]:
        st.header("Portfolio Strategies")
        
        st.subheader("Strategic Asset Allocation")
        st.write("""
        This long-term approach focuses on creating a portfolio based on your risk tolerance, time horizon, and financial goals.
        It maintains a target asset allocation regardless of short-term market conditions.
        
        **Example:**
        A moderate risk investor might maintain a 60% stocks, 30% bonds, and 10% cash allocation over many years.
        """)
        
        st.subheader("Tactical Asset Allocation")
        st.write("""
        This approach allows short-term deviations from the strategic allocation to capitalize on market opportunities
        or mitigate risks based on market forecasts.
        
        **Example:**
        Temporarily increasing bond allocation during periods of high stock market volatility.
        """)
        
        st.subheader("Dollar-Cost Averaging")
        st.write("""
        Dollar-cost averaging involves investing a fixed amount of money at regular intervals,
        regardless of market conditions. This strategy helps avoid the risk of investing all your money
        at an unfavorable time and can reduce the impact of market volatility.
        
        **Benefits:**
        - Removes emotion from investment decisions
        - Reduces impact of market timing
        - Creates discipline in saving and investing
        """)
        
        st.subheader("Value Investing")
        st.write("""
        Value investing focuses on finding securities trading below their intrinsic value,
        based on fundamental analysis.
        
        **Key Metrics:**
        - Price-to-earnings (P/E) ratio
        - Price-to-book (P/B) ratio
        - Dividend yield
        - Free cash flow
        """)
        
        st.subheader("Growth Investing")
        st.write("""
        Growth investing focuses on companies expected to grow faster than the market average,
        even if they currently trade at high valuations.
        
        **Key Metrics:**
        - Revenue growth rate
        - Earnings growth rate
        - Return on equity (ROE)
        - Market opportunity and competitive position
        """)
    
    # Market Analysis tab
    with tabs[4]:
        st.header("Market Analysis")
        
        st.subheader("Fundamental Analysis")
        st.write("""
        Fundamental analysis evaluates securities by examining related economic, financial, and other qualitative and quantitative factors.
        
        **Components of Fundamental Analysis:**
        - Economic analysis: GDP growth, inflation, interest rates, employment
        - Industry analysis: Competitive landscape, growth prospects, regulatory environment
        - Company analysis: Financial statements, management quality, competitive advantages
        
        **Key Financial Metrics:**
        - Earnings per share (EPS)
        - Price-to-earnings (P/E) ratio
        - Return on equity (ROE)
        - Debt-to-equity ratio
        - Free cash flow
        """)
        
        st.subheader("Technical Analysis")
        st.write("""
        Technical analysis evaluates securities by analyzing statistics generated by market activity,
        such as past prices and volume, to identify patterns that may suggest future activity.
        
        **Common Technical Indicators:**
        - Moving averages
        - Relative strength index (RSI)
        - MACD (Moving Average Convergence Divergence)
        - Bollinger Bands
        - Support and resistance levels
        """)
        
        st.subheader("Economic Indicators")
        st.write("""
        Economic indicators are statistics that provide insights into the overall health and direction of an economy.
        
        **Key Economic Indicators:**
        - Gross Domestic Product (GDP)
        - Unemployment rate
        - Consumer Price Index (CPI) for inflation
        - Consumer Confidence Index
        - Housing starts and permits
        - Purchasing Managers' Index (PMI)
        """)
        
        st.subheader("Market Cycles")
        st.write("""
        Markets typically move in cycles, with periods of expansion (bull markets) and contraction (bear markets).
        Understanding where we are in a market cycle can help inform investment decisions.
        
        **Stages of a Market Cycle:**
        1. Accumulation: Smart money begins buying after a market bottom
        2. Mark-up: Prices begin trending upward as economic conditions improve
        3. Distribution: Smart money begins selling near market peaks
        4. Mark-down: Prices trend downward, often accompanied by economic deterioration
        """)
    
    return tabs
