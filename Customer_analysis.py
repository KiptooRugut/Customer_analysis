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
    
def plot_customer_distribution_by_year(df):
    """Plot customer distribution by subscription year"""
    plt.figure(figsize=(14, 8))
    ax = sns.countplot(data=df, x='Subscription Year', palette='viridis')
    
    # Add value labels
    for p in ax.patches:
        ax.annotate(f'{p.get_height()}', 
                   (p.get_x() + p.get_width()/2., p.get_height()), 
                   ha='center', va='center', 
                   xytext=(0, 10), 
                   textcoords='offset points')
    
    plt.title('Customer Distribution by Subscription Year', fontsize=18)
    plt.xlabel('Subscription Year', fontsize=14)
    plt.ylabel('Number of Customers', fontsize=14)
    plt.tight_layout()
    plt.savefig('customer_distribution_by_year.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Created customer distribution by year plot")