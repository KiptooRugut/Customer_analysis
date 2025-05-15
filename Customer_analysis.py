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


def plot_monthly_subscriptions(df):
    """Plot monthly subscriptions over time"""
    monthly_data = df.groupby('Subscription Year-Month').size()
    
    plt.figure(figsize=(16, 8))
    monthly_data.plot(kind='line', marker='o', color='royalblue', linewidth=2.5)
    
    plt.title('Monthly Customer Subscriptions Over Time', fontsize=18)
    plt.xlabel('Year-Month', fontsize=14)
    plt.ylabel('Number of Subscriptions', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('monthly_subscriptions.png', dpi=300)
    plt.close()
    print("Created monthly subscriptions plot")

def plot_top_countries(df, n=15):
    """Plot top countries by customer count"""
    top_countries = df['Country'].value_counts().head(n)
    
    plt.figure(figsize=(14, 8))
    sns.barplot(x=top_countries.values, y=top_countries.index, palette='rocket')
    
    plt.title(f'Top {n} Countries by Customer Count', fontsize=18)
    plt.xlabel('Number of Customers', fontsize=14)
    plt.ylabel('Country', fontsize=14)
    plt.tight_layout()
    plt.savefig('top_countries.png', dpi=300)
    plt.close()
    print(f"Created top {n} countries plot")

def plot_year_distribution_by_country(df, n=10):
    """Plot subscription year distribution by country"""
    plt.figure(figsize=(14, 8))
    
    # Convert to integer years
    df['Subscription Year'] = df['Subscription Year'].astype(int)
    top_countries = df['Country'].value_counts().head(n).index
    
    ax = sns.boxplot(data=df, 
                    x='Subscription Year', 
                    y='Country',
                    order=top_countries,
                    palette='Set3')
    
    plt.title(f'Subscription Year Distribution by Country (Top {n})', fontsize=18)
    plt.xlabel('Subscription Year', fontsize=14)
    plt.ylabel('Country', fontsize=14)

    # Set proper year ticks
    years = sorted(df['Subscription Year'].unique())
    ax.set_xticks(years)
    ax.set_xticklabels(years)
    ax.yaxis.grid(True, linestyle='--', alpha=0.4)
    
    plt.tight_layout()
    plt.savefig('year_distribution_by_country.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Created year distribution by country plot (top {n})")


def main():
    print("Customer Data Analysis\n" + "="*50 + "\n")
    
    # Configure plot settings
    configure_plot_settings()
    
    # Load and prepare data
    df = load_and_prepare_data()  # Removed the argument since we hardcoded the filename
    if df is None:
        return
    
    # Create visualizations
    plot_customer_distribution_by_year(df)
    plot_monthly_subscriptions(df)
    plot_top_countries(df)
    plot_year_distribution_by_country(df)
    
    print("\nAnalysis complete! Check the generated PNG files for visualizations.")


if __name__ == "__main__":
    main()