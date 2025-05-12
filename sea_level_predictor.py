import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress



def draw_plot():
    # Read data from file
    df= pd.read_csv('epa-sea-level.csv')
    df_2000 = df[df['Year'] >= 2000]

    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])

    x_pred = pd.Series(range(1880, 2051))  # Full range to 2050
    y_pred = res.intercept + res.slope * x_pred

    x_pred_2000 = pd.Series(range(2000, 2051))
    y_pred_2000 = res_2000.intercept + res_2000.slope * x_pred_2000

    # Create scatter plot
    plt.figure(figsize=(12, 6))  # Create and size the figure FIRST
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=10, label='Original Data')

    # Create first line of best fit
    plt.plot(x_pred, y_pred, 'r', label='Best Fit Line')

    # Create second line of best fit
    plt.plot(x_pred_2000, y_pred_2000, 'b', label='Best Fit Line (2000 onwards)')

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.grid(True)
    plt.legend()    
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()