# The pandas library is used for data manipulation, the matplot is the main library for creating plots, 
# and the seaborn library is used to expand matplot and make it simpler to write.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Starting the script...")

# Load the dataset into variable data
data = pd.read_csv('Housing.csv')
print("Data loading complete.")

# Data Cleaning
# There were some missing values so the cleans the data by assuming a missing value means it should be no/0
data.fillna({
    'sqft_basement': 0, 
    'yr_renovated': 0,
}, inplace=True)

# This converts the date column to datetime format so we can use that information
data['date'] = pd.to_datetime(data['date'])
data['year'] = data['date'].dt.year
data['month'] = data['date'].dt.month

print("Data cleaning complete.")

# Set the style of the charts
sns.set_style("whitegrid")
sns.set_palette("pastel")

# This is important for creating charts in matplot. It set the size of the charts and the amount of rows/columns
fig, axes = plt.subplots(2, 3, figsize=(20, 12)) 

# Chart 1: Price Trends Over Time
sns.lineplot(x='date', y='price', data=data, ax=axes[0, 0], color='blue', linewidth=2.5)
axes[0, 0].set_title('Housing Prices Over Time')
axes[0, 0].yaxis.set_major_formatter('${x:,.0f}')
axes[0, 0].set_xlabel('Date')
axes[0, 0].set_ylabel('Price')
axes[0, 0].tick_params(axis='x', rotation=45)

# CHart 2: Price Distribution by Number of Bedrooms
sns.boxplot(x='bedrooms', y='price', data=data, ax=axes[0, 1], hue='bedrooms', palette='muted', legend=False)
axes[0, 1].set_title('Price Distribution by Number of Bedrooms')
axes[0, 1].yaxis.set_major_formatter('${x:,.0f}')
axes[0, 1].set_xlabel('Number of Bedrooms')
axes[0, 1].set_ylabel('Price')

# Chart 3: Average Housing Price by Zipcode
avg_price_by_zipcode = data.groupby('zipcode')['price'].mean().sort_values(ascending=False)
sns.barplot(x=avg_price_by_zipcode.index, y=avg_price_by_zipcode.values, ax=axes[0, 2], hue=avg_price_by_zipcode.index, palette='viridis', legend=False)
axes[0, 2].set_title('Average Housing Price by Zipcode')
axes[0, 2].tick_params(axis='x', rotation=90)
axes[0, 2].tick_params(axis='x', labelsize=6) 
axes[0, 2].yaxis.set_major_formatter('${x:,.0f}')
axes[0, 2].set_xlabel('Zipcode')
axes[0, 2].set_ylabel('Average Price')

# Chart 4: Price vs. Sqft Living
sns.scatterplot(x='sqft_living', y='price', data=data, ax=axes[1, 0], color='purple', s=10)
axes[1, 0].set_title('Price vs. Sqft Living')
axes[1, 0].yaxis.set_major_formatter('${x:,.0f}')
axes[1, 0].set_xlabel('Sqft Living')
axes[1, 0].set_ylabel('Price')

# Chart 5: Average Price vs. Year Built (starting from 1940)
avg_price_by_year_built = data[data['yr_built'] >= 1940].groupby('yr_built')['price'].mean().sort_index()
sns.lineplot(x=avg_price_by_year_built.index, y=avg_price_by_year_built.values, ax=axes[1, 1], color='green', linewidth=2.5)
axes[1, 1].set_title('Average Price vs. Year Built')
axes[1, 1].yaxis.set_major_formatter('${x:,.0f}')
axes[1, 1].set_xlim(1940, data['yr_built'].max())
axes[1, 1].set_xlabel('Year Built')
axes[1, 1].set_ylabel('Average Price')

# Chart 6: Price Distribution by Condition
sns.boxplot(x='condition', y='price', data=data, ax=axes[1, 2], hue='condition', palette='coolwarm', legend=False)
axes[1, 2].set_title('Price Distribution by Condition')
axes[1, 2].yaxis.set_major_formatter('${x:,.0f}')
axes[1, 2].set_xlabel('Condition')
axes[1, 2].set_ylabel('Price')

print("Generating plots...")
# Adjust layout to show all charts at once
plt.tight_layout()
plt.show()

print("Analysis complete.")