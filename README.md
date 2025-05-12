# 📊 Sea Level Predictor

In this project, you will analyze a dataset of the global average sea level change since 1880. Using this historical data, you will build a model to predict sea level change through the year 2050.

## Tasks

- Use **Pandas** to import the data from `epa-sea-level.csv`.
- Use **Matplotlib** to create a **scatter plot** with:
  - `Year` as the x-axis
  - `CSIRO Adjusted Sea Level` as the y-axis
- Use the `linregress` function from **scipy.stats** to:
  - Calculate the **slope** and **intercept** of the line of best fit.
  - Plot the line of best fit over the scatter plot.
  - Extend the line through the year **2050** to predict future sea level rise.
- Create a **second line of best fit** using only the data from **2000 onward**:
  - Again, use `linregress` to find the slope and intercept.
  - Plot this line and extend it through **2050** to show the more recent trend.
- Label the plot:
  - **X-axis**: `Year`
  - **Y-axis**: `Sea Level (inches)`
  - **Title**: `Rise in Sea Level`

## Goal

Visualize sea level trends and use linear regression to predict how sea levels might change by 2050, both based on the full dataset and the more recent trend since 2000.
