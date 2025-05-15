# customer_analysis.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from sklearn.model_selection import train_test_split


def configure_plot_settings():
    """Configure matplotlib and seaborn settings for consistent visualizations"""
    sns.set_style("whitegrid")
    plt.rcParams['figure.figsize'] = (12, 7)
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.labelsize'] = 14
    plt.rcParams['axes.titlesize'] = 16
    plt.rcParams['xtick.labelsize'] = 12
    plt.rcParams['ytick.labelsize'] = 12

def load_and_prepare_data():
    """Load and prepare the customer data"""
    try:
        df = pd.read_csv('customers-1000.csv')  # Fixed: Directly specify filename
        print("Dataset loaded successfully!")
        
        # Convert and extract date features
        df['Subscription Date'] = pd.to_datetime(df['Subscription Date'])
        df['Subscription Year'] = df['Subscription Date'].dt.year
        df['Subscription Month'] = df['Subscription Date'].dt.month
        df['Subscription Year-Month'] = df['Subscription Date'].dt.to_period('M')
        
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None