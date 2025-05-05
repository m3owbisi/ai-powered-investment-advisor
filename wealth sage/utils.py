import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
from io import BytesIO
from datetime import datetime, timedelta

def load_profile_image(risk_profile):
    """
    Return a URL for an image representing the risk profile.
    
    Args:
        risk_profile (str): Risk profile category
        
    Returns:
        str: URL to an image representing the risk profile
    """
    # Using Feather Icons for profile images
    icon_map = {
        "Conservative": "https://cdn.jsdelivr.net/gh/feathericons/feather@4.29.0/icons/shield.svg",
        "Moderately Conservative": "https://cdn.jsdelivr.net/gh/feathericons/feather@4.29.0/icons/anchor.svg",
        "Moderate": "https://cdn.jsdelivr.net/gh/feathericons/feather@4.29.0/icons/activity.svg",
        "Moderately Aggressive": "https://cdn.jsdelivr.net/gh/feathericons/feather@4.29.0/icons/trending-up.svg",
        "Aggressive": "https://cdn.jsdelivr.net/gh/feathericons/feather@4.29.0/icons/target.svg"
    }
    
    return icon_map.get(risk_profile, "https://cdn.jsdelivr.net/gh/feathericons/feather@4.29.0/icons/help-circle.svg")

def format_currency(amount):
    """
    Format a number as currency.
    
    Args:
        amount (float): Amount to format
        
    Returns:
        str: Formatted currency string
    """
    return "${:,.2f}".format(amount)

def format_percentage(value):
    """
    Format a decimal as a percentage.
    
    Args:
        value (float): Value to format (e.g., 0.05 for 5%)
        
    Returns:
        str: Formatted percentage string
    """
    return "{:.2f}%".format(value * 100)

def generate_color_scale(n_colors, palette="blues"):
    """
    Generate a color scale for visualizations.
    
    Args:
        n_colors (int): Number of colors to generate
        palette (str): Color palette name
        
    Returns:
        list: List of color hex codes
    """
    # Basic color palettes (could be expanded in a production app)
    palettes = {
        "blues": ["#C6DBEF", "#9ECAE1", "#6BAED6", "#4292C6", "#2171B5", "#084594"],
        "greens": ["#C7E9C0", "#A1D99B", "#74C476", "#41AB5D", "#238B45", "#005A32"],
        "reds": ["#FCBBA1", "#FC9272", "#FB6A4A", "#EF3B2C", "#CB181D", "#99000D"],
        "purples": ["#DADAEB", "#BCBDDC", "#9E9AC8", "#807DBA", "#6A51A3", "#4A1486"],
        "oranges": ["#FDD0A2", "#FDAE6B", "#FD8D3C", "#F16913", "#D94801", "#8C2D04"]
    }
    
    selected_palette = palettes.get(palette, palettes["blues"])
    
    # If we need more colors than in the basic palette, we interpolate
    if n_colors <= len(selected_palette):
        return selected_palette[:n_colors]
    else:
        # Simple interpolation (in a real app, would use a proper color library)
        indices = np.linspace(0, len(selected_palette)-1, n_colors)
        return [selected_palette[int(i)] for i in indices]
